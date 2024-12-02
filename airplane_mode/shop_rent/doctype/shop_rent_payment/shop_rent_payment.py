# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopRentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		payment_amount: DF.Currency
		payment_date: DF.Date
		shop: DF.Link
		status: DF.Literal["Pending", "Paid"]
		tenant: DF.Link
	# end: auto-generated types
	pass
