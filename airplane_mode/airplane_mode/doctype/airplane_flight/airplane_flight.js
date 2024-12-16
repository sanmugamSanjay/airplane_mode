// Copyright (c) 2024, Sanmugam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
    refresh(frm) {
        if(!frm.is_new()){
        let d = new frappe.ui.Dialog({
            title: 'Select Gate',
            fields: [
                {
                    "default": "GT-1",
                    "fieldname": "gate_no",
                    "fieldtype": "Select",
                    "label": "Gate No",
                    "options": "GT-1\nGT-2\nGT-3\nGT-4\nGT-5"
                   }
            ],
            size: 'small',
            primary_action_label: 'Assign',
            primary_action(values) {
                console.log(values)
                if (frm.doc.gate_no) {
                    frm.set_value("gate_no",values.gate_no)
                    frappe.call({
                        method: "change_gate_number",
                        doc:frm.doc,
                        //function not return anything
                        callback: function(response) {
                            if (response.message) {
                                console.log(response)
                            } 
                        }
                    });
                } else {
                    frappe.msgprint("Please select a flight before fetching capacity.");
                }
                d.hide();
                frm.reload_doc()
            }
        });

        frm.add_custom_button("Assign Gate", () => {
            d.show();
        }, "Action");
    }
}
});
