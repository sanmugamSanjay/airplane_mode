# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Airport(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		available_count: DF.Int
		city: DF.Data
		code: DF.Data
		country: DF.Data
		location_name: DF.Data
		logo: DF.AttachImage | None
		occupied_count: DF.Int
		state: DF.Data
		total_count: DF.Int
		zip_code: DF.Data
	# end: auto-generated types
	pass
