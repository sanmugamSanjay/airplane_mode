# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status="Completed"
	def before_save(self):
		self.title=f"{self.airplane}"
		self.route=f"flights/{self.name}"
