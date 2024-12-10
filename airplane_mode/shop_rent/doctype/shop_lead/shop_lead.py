# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopLead(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport_shop: DF.Link
		amended_from: DF.Link | None
		description: DF.SmallText | None
		email: DF.Data
		name1: DF.Data
		phone_no: DF.Phone
		status: DF.Literal["New Lead", "Contacted", "Lease Offered", "Lease Signed", "Closed (Rented)", "Closed (Not Rented)"]
	# end: auto-generated types
	pass
