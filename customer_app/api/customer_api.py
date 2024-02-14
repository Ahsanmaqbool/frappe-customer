import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_customer(fullname, email, address, telephone):
    customer = frappe.get_doc({
        "doctype": "Client",
        "fullname": fullname,
        "email": email,
        "address": address,
        "telephone": telephone
    })
    customer.insert(ignore_permissions=True)
    return _("Customer {0} created successfully.").format(fullname)


@frappe.whitelist(allow_guest=True)
def get_customers():
    return frappe.get_all("Client", fields=["fullname", "email", "address", "telephone"])