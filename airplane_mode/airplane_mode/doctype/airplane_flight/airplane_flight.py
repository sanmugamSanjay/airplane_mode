# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.crew_member.crew_member import CrewMember
		from frappe.types import DF

		airplane: DF.Link
		amended_from: DF.Link | None
		crew_members: DF.Table[CrewMember]
		date_of_departure: DF.Date
		destination_airport: DF.Link
		destination_airport_code: DF.Data | None
		duration: DF.Duration
		gate_no: DF.Literal["GT-1", "GT-2", "GT-3", "GT-4", "GT-5"]
		is_published: DF.Check
		new_gate_no: DF.Data | None
		route: DF.Data | None
		source_airport: DF.Link
		source_airport_code: DF.Data | None
		status: DF.Literal["Scheduled", "Completed", "Cancelled"]
		time_of_departure: DF.Time
	# end: auto-generated types
	def on_submit(self):
		self.status="Completed"
	def before_save(self):
		self.title=f"{self.airplane}"
		self.route=f"flights/{self.name}"
	
	@frappe.whitelist()
	def change_gate_number(self):
		try:
			self.save()
			previous_doc = self.get_doc_before_save()
			
			tickets = frappe.db.get_list(
				"Airplane Ticket",
				filters={"status": "Booked", "flight": self.name},
				fields=["name", "passenger"]
			)

			email_message = f"""
			<p>Dear Sir/Madam,</p>
			<p>We are writing to inform you of an update to your flight details. Please review the revised information below:</p>
			<p>Departure Gate: {previous_doc.gate_no} → {self.gate_no}</p>
			<p>We recommend arriving at the airport well in advance to accommodate the new gate and any necessary preparations.</p>
			<p>If you have any questions or require assistance, please contact us at support@gmail.com.</p>
			<p>Thank you for your understanding and cooperation. We look forward to serving you.</p>
			<p>Safe travels,<br> Customer Service Team</p>
			"""

			for ticket in tickets:
				ticket_doc = frappe.get_doc("Airplane Ticket", ticket["name"])
				passenger_doc = frappe.get_doc("Flight Passenger", ticket["passenger"])
				ticket_doc.gate_no = self.gate_no

				# frappe.errprint(email_message)
				# frappe.errprint(passenger_doc.email)

				subject = "Important Update: Flight Details Changed"
				frappe.sendmail(
					recipients=passenger_doc.email,
					subject=subject,
					message=email_message,
					delayed=False,
					retry=3
				)
				ticket_doc.save()

			frappe.db.commit()

			frappe.msgprint(f"Gate number updated successfully for flight {self.name}.")
		except Exception as e:
			frappe.db.rollback()
			frappe.log_error(f"Error updating gate number for flight {self.name}: {str(e)}", "Gate Update Error")
			frappe.throw("Could not update gate number. Please check the logs for more details.")
