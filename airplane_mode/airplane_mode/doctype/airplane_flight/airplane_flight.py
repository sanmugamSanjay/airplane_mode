# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
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
