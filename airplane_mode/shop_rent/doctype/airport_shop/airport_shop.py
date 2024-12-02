# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShop(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		amount: DF.Currency
		area_in_sq: DF.Float
		end_date: DF.Date | None
		shop_number: DF.Data
		start_date: DF.Date | None
		status: DF.Literal["Available", "Occupied"]
		tenant: DF.Link | None
	# end: auto-generated types

	def before_insert(self):
		update_airport_count(self,"create")
	
	def before_save(self):
		if not self.is_new():
			update_airport_count(self,"update")
		shop_settings=frappe.get_doc("Airport Shop Settings")
		standard_amount_for_sq=shop_settings.standard_rent_amount
		self.amount= standard_amount_for_sq * self.area_in_sq
				
	def on_trash(self):
		if not self.is_canceled:
			update_airport_count(self, "delete")

	def on_cancel(self):
		self.is_canceled = True
		self.save() 
		update_airport_count(self, "cancel")


def update_airport_count(self, action):
    airport = frappe.get_doc("Airport", self.airport)
    previous_doc = self.get_doc_before_save() if action == "update" else None

    if action == "update":
        if previous_doc and self.status != previous_doc.status:
            if self.status == "Available":
                airport.available_count += 1
                airport.occupied_count -= 1
            elif self.status == "Occupied":
                airport.occupied_count += 1
                airport.available_count -= 1
    elif action == "create":
        airport.total_count = airport.total_count + 1
        if self.status == "Available":
            airport.available_count += 1
        else:
            airport.occupied_count += 1
    elif action in ["cancel", "delete"]:
        airport.total_count -= 1
        if self.status == "Available":
            if airport.available_count > 0:  
                airport.available_count -= 1
        elif self.status == "Occupied":
            if airport.occupied_count > 0:  
                airport.occupied_count -= 1
    airport.save()


def create_rent_payment_for_shop(shop_name):
    shop = frappe.get_doc("Airport Shop", shop_name)
    
    if shop.tenant:
        tenant = shop.tenant
        rent_amount = shop.rent_amount
        
        existing_payment = frappe.db.exists(
            "Shop Rent Payment",
            {"tenant": tenant, "shop": shop_name, "payment_date": frappe.utils.today()}
        )
        
        if not existing_payment:
            rent_payment = frappe.get_doc({
                "doctype": "Shop Rent Payment",
                "tenant": tenant,
                "shop": shop_name,
                "payment_amount": rent_amount,
                "payment_date": frappe.utils.today(),
                "status": "Pending"
            })
            rent_payment.insert()
            frappe.db.commit()
            frappe.msgprint(f"Rent Payment created for {tenant} in shop {shop_name}.")
