// Copyright (c) 2024, Sanmugam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Shop", {
	refresh(frm) {
        if(!frm.is_new()){
        let d = new frappe.ui.Dialog({
            title: 'Select Gate',
            fields: [
                {
                 "fieldname": "tenant",
                 "fieldtype": "Link",
                 "label": "Tenant",
                 "options": "Tenant"
                },
                {
                    "fieldname": "start_date",
                    "fieldtype": "Date",
                    "label": "start Date"
                   },
                               {
                    "fieldname": "end_date",
                    "fieldtype": "Date",
                    "label": "End Date"
                   }
            ],
            size: 'small',
            primary_action_label: 'Assign',
            primary_action(values) {
                console.log(values)
                    frm.set_value("tenant",values.tenant)
                    frm.set_value("end_date",values.end_date)
                    frm.set_value("start_date",values.start_date)
                    frm.set_value("status","Occupied")
                    frappe.call({
                        method: "assign_tenant",
                        doc:frm.doc,
                        //function not return anything
                        callback: function(response) {
                            console.log(response)
                            if (response?.message) 
                                frappe.msgprint(response?.message);
                            
                        }
                    });
                
                d.hide();
                frm.reload_doc()
            }
        });
        let label= frm.doc.status === "Available" ? "Assign Tenat":"Re-Assign Tenat"
     
            
        
        frm.add_custom_button(label, () => {
            d.show();
        }, "Action");
        
    }
}
});
