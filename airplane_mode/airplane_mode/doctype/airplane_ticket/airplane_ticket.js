// Copyright (c) 2024, Sanmugam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        let d = new frappe.ui.Dialog({
            title: 'Select Seat',
            fields: [
                {
                    label: 'Seat Number',
                    fieldname: 'seat',
                    fieldtype: 'Int'
                }
            ],
            size: 'small',
            primary_action_label: 'Assign',
            primary_action(values) {
                console.log(values)
                capacity=0;
                if (frm.doc.flight) {
                    frappe.call({
                        method: "airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.get_capacity",
                        args: {
                            flight: frm.doc.flight
                        },
                        callback: function(response) {
                            if (response.message) {
                                if(values.seat >response.message )
                                    frappe.msgprint(`Selected seat-${values.seat} greater then the Capacity`);
                            } else {
                                frappe.msgprint("No capacity found for the selected flight.");
                            }
                        }
                    });
                } else {
                    frappe.msgprint("Please select a flight before fetching capacity.");
                }
                frm.set_value('seat', values.seat)
                d.hide();
            }
        });

        frm.add_custom_button("Assign Seat", () => {
            d.show();
        }, "Action");
    },
    validate: function (frm) {
        console.log("check the add ons", frm.doc.add_ons)
        if (frm.doc.add_ons.length > 0) {
            let unsaved_arr = [...frm.doc.add_ons].filter((item) => item?.__unsaved);
            let db_ex_arr = [...frm.doc.add_ons].filter((item) => item.__unsaved === undefined);
            err_name = ""
            for (let item of unsaved_arr) {
                console.log("inside Loop", item.item)
                if (db_ex_arr.some((data) => data.item === item.item)) {
                    frappe.validated = false
                    console.log("inside Loop 2", item.item)
                    frappe.msgprint(
                        msg = 'Item Already exist ' + item.item,
                        title = 'Error',
                    )
                    break
                }
            }
        }
    },
    update_total_amount(frm) {
        let total_add_on_amount = 0
        for (let add_on of frm.doc.add_ons)
            total_add_on_amount = total_add_on_amount + add_on.amount

        let total_amount = frm.doc.flight_price + total_add_on_amount
        frm.set_value("total_amount", total_amount)

    },
    flight_price(frm) {
        frm.trigger("update_total_amount")
    }
});

frappe.ui.form.on("Airplane Ticket Add-on Item", {
    validate(frm) {
        console.log("check existing data", frm.name)
    },
    add_ons_add(frm, cdt, cdn) {
        frm.trigger("update_total_amount")
    },
    add_ons_remove(frm, cdt, cdn) {
        frm.trigger("update_total_amount")
    },
    amount(frm, cdt, cdn) {
        frm.trigger("update_total_amount")
    }
});