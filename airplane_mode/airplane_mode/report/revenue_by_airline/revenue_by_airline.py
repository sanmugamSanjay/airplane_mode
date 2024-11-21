# Copyright (c) 2024, Sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()
	chart=get_chart(data)
	message="Detailed revenue report by airline"

	return columns, data, message, chart, None


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Data",
		},
		{
			"label": _("Revenue"),
			"fieldname": "revenue",
			"fieldtype": "Int",
		},
	]


def get_data() -> list[list]:
	data = frappe.db.sql("""
	select t.name as airline,IFNULL(SUM(t3.total_amount), 0) as revenue from `tabAirline` t
  	left join `tabAirplane` t1 on t.name=t1.airline
  	left join `tabAirplane Flight` t2 on t1.name=t2.airplane
  	left join `tabAirplane Ticket` t3 on t2.name=t3.flight group by t.name""",as_dict=True)


	return data

def get_chart(data):
	return {
		"data":{
			"labels":[d["airline"] for d in data],
			"dataset": [{"name":"Revenue By Airline","values":[d["revenue"] for d in data]}],
			"type":"donut"
		}
	}
