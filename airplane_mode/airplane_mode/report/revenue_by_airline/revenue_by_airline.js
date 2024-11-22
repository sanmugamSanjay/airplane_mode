// Copyright (c) 2024, Sanmugam and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Airline"] = {
	filters: [
		// {
		// 	"fieldname": "my_filter",
		// 	"label": __("My Filter"),
		// 	"fieldtype": "Data",
		// 	"reqd": 1,
		// },
	],
	formatter: function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (data["airline"] === "Total") {
			value = value.bold()
		} 
		return value;
	}
};
