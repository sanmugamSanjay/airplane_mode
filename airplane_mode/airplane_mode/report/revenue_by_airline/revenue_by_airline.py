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
	# frappe.errprint(columns)
	data = get_data()
	# frappe.errprint(data)
	chart=get_chart(data)
	# frappe.errprint(chart)
	message="Detailed revenue report by airline"
	total=0
	for d in data:
		total=total+d["revenue"]
	data.append({"airline":"Total",
	"revenue":total})

	report_summary=[{
				"value": total,
				"indicator": "Green",
				"label": _("Total Revenue"),
				"datatype": "Currency",
			}]

	return columns, data, message, chart, report_summary


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": 100
		},
		{
			"label": _("Revenue"),
			"fieldname": "revenue",
			"fieldtype": "Currency",
			"width":150
		},
	]


def get_data() -> list[list]:
	data = frappe.db.sql("""
	select t.name as airline,IFNULL(SUM(t3.total_amount), 0) as revenue from `tabAirline` t
  	left join `tabAirplane` t1 on t.name=t1.airline
  	left join `tabAirplane Flight` t2 on t1.name=t2.airplane
  	left join `tabAirplane Ticket` t3 on t2.name=t3.flight group by t.name""",as_dict=True)
	# frappe.errprint(data)

	return data

def get_chart(data):
	return {
		"data":{
			"labels":[d["airline"] for d in data],
			"datasets": [{"name":"Revenue By Airline","values":[d["revenue"] for d in data]}],
			"type":"donut",
			"colors":["red","blue","green"]
		}
	}
