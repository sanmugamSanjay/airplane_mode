# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import random


class AirplaneTicket(Document):
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
