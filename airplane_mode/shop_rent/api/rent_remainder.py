import frappe
from frappe import _
from frappe.utils import today, add_days

@frappe.whitelist()
def send_rent_reminders():
    enable_reminders = frappe.db.get_single_value("Airport Shop Settings", "enable_rent_reminders")
    if not enable_reminders:
        return

    # Get tenant assigned shops
    query_str="""
    SELECT t.name, t.shop_number, t.amount, t.airport, t.tenant, t1.email
    FROM `tabAirport Shop` t
    LEFT JOIN `tabTenant` t1 ON t.tenant = t1.name
    WHERE t.start_date <= %(cur_day)s AND t.end_date >= %(cur_day)s
    """

    # query_str="""
    # SELECT t.name, t.shop_number, t.amount, t.airport, t.tenant, t1.email
    # FROM `tabAirport Shop` t
    # LEFT JOIN `tabTenant` t1 ON t.tenant = t1.name
    # WHERE t.start_date <=
    # """
    # query_str=query_str+_("'{0}' AND t.end_date >= '{0}'").format(today())

    # shops=frappe.db.sql(query_str, as_dict=True)
    shops=frappe.db.sql(query_str,{"cur_day":today()}, as_dict=True)

    if shops:
        for shop in shops:
            obj = {
                "recipients": shop.email,
                "subject": "Rent Payment Reminder",
                "message": f"""
                    <p>Dear {shop.tenant_name},</p>
                    <p>Your rent payment is due for the following shop:</p>
                    <p>Shop Name: {shop.name}</p>
                    <p>Amount Due: {shop.amount}</p>
                    <p>Please make the payment at the earliest to avoid any penalties.</p>
                """,
            }
            try:
                frappe.sendmail(
                    recipients=obj["recipients"],
                    subject=obj["subject"],
                    message=obj["message"],
                )
                print(f"Mail sent to {shop.email}")
            except Exception as e:
                print(f"Failed to send mail to {shop.email}: {str(e)}")
        return "Mail sent"
    else:
        return "No shop found"


    # if shops:
    #     for shop in shops:
    #         obj={
    #             "recipients":shop.email,
    #             "subject":"Rent Payment Reminder",
    #             "message":f"""
    #                 <p>Dear {shop.tenant_name},</p>
    #                 <p>Your rent payment is due for the following shop:</p>
    #                 <p>Shop Name: {shop.name}</p>
    #                 <p>Amount Due: {shop.amount}</p>
    #                 <p>Please make the payment at the earliest to avoid any penalties.</p>
    #             """
    #         }
    #         print(obj)
    #         frappe.sendmail(obj)
    #     return "mail send"
    # else:
    #     return "no shop found"

        

   