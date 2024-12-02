# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tenant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data
		phone_no: DF.Phone
	# end: auto-generated types
	pass
