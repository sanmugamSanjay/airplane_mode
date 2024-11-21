// Copyright (c) 2024, Sanmugam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        if(frm.doc.website){
            frm.sidebar.add_user_action("visit website",()=>{
                window.open(frm.doc.website,'_blank')
            })
            // frm.add_custom_button("visit website",()=>{
            //     window.open(frm.doc.website,'_blank')
            // })
            // .addClass('btn-primary')
        }
	},
});
