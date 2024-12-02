# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirportShopSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		area_type: DF.Literal["SQ Meter", "Feet"]
		enable_rent_reminders: DF.Check
		standard_rent_amount: DF.Currency
	# end: auto-generated types
	pass
