import frappe
from frappe.utils import today, add_days

def send_rent_reminders():
    enable_reminders = frappe.db.get_single_value("Airport Shop Settings", "enable_rent_reminders")
    if not enable_reminders:
        return

    
    # tenants = frappe.get_all("Tenant", fields=["name", "email"])

    # for tenant in tenants:
    #     unpaid_shops = frappe.db.sql("""
    #         SELECT shop.name, shop.rent_amount 
    #         FROM `tabShop` shop
    #         LEFT JOIN `tabRent Payment` rent
    #         ON shop.name = rent.shop
    #         WHERE shop.tenant = %s AND (rent.payment_date IS NULL OR rent.payment_date < %s)
    #     """, (tenant.name, today()), as_dict=True)

    #     if unpaid_shops:
    #         shop_list = "<ul>"
    #         for shop in unpaid_shops:
    #             shop_list += f"<li>Shop: {shop.name} - Rent Amount: {shop.rent_amount}</li>"
    #         shop_list += "</ul>"

    #         frappe.sendmail(
    #             recipients=tenant.email,
    #             subject="Rent Payment Reminder",
    #             message=f"""
    #                 <p>Dear {tenant.name},</p>
    #                 <p>Your rent is due for the following shops:</p>
    #                 {shop_list}
    #                 <p>Please make the payment at the earliest to avoid any penalties.</p>
    #             """
    #         )
