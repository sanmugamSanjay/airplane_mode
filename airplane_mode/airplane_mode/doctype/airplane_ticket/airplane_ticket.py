# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import random


class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
		from frappe.types import DF

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date | None
		departure_time: DF.Time | None
		destination_airport_code: DF.Data | None
		duration_of_flight: DF.Duration | None
		flight: DF.Link
		flight_price: DF.Currency
		gate_no: DF.Literal["GT-1", "GT-2", "GT-3", "GT-4", "GT-5", "GT-6"]
		passenger: DF.Link
		seat: DF.Data | None
		source_airport_code: DF.Data | None
		status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types
	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw("Status not equlat to boarded")

	def before_save(self):
		capacity=self.get_capacity_by_flight(self.flight)
		frappe.errprint(capacity)
		total=0
		if len(self.add_ons) > 0: 
			total=self.calculation(self.add_ons)
		self.total_amount=self.flight_price +total
	
	def calculation(self,items):
		total=0
		for item in items:
			total=total+item.amount
		return total
		
	def before_insert(self):
		capacity=self.get_capacity_by_flight(self.flight)
		# frappe.errprint(capacity)
		d = random.randint(1, capacity)
		rd = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{d}{rd}"

	
	def get_capacity_by_flight(self,flight):
		capacity=0
		flight=frappe.get_doc("Airplane Flight",flight)
		if flight.airplane is not None:
			data=flight.airplane.split("-")
			name=data[0]+"-"+data[1]
			plane=frappe.get_doc("Airplane",name)
			capacity=plane.capacity
		return capacity

	def validate(self):
		if len(self.add_ons) > 0:
			items = []
			for data in self.add_ons:
				if data.item in items:
					frappe.throw(_("Item ({0}) already exists").format(data.item))
				else:
					items.append(data.item)

@frappe.whitelist()
def get_capacity(flight):
	capacity=0
	flight=frappe.get_doc("Airplane Flight",flight)
	if flight.airplane is not None:
		data=flight.airplane.split("-")
		name=data[0]+"-"+data[1]
		plane=frappe.get_doc("Airplane",name)
		capacity=plane.capacity
	return capacity

@frappe.whitelist()
def check_ticket(seat,flight):
	seat = int(seat)
	capacity=get_capacity(flight)
	if seat > capacity:
		frappe.throw(_("Selected seat-{0} greater then the Capacity").format(seat))
	return capacity