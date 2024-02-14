from . import __version__ as app_version
from frappe import _

app_name = "customer_app"
app_title = "Customer App"
app_publisher = "Ahsan Maqbool"
app_description = "Customer Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@creative.com"
app_license = "MIT"


def get_data():
    return [
        {
            "label": _("Documents"),
            "icon": "octicon octicon-file-directory",
            "items": [
                {
                    "type": "doctype",
                    "name": "Customer",
                    "label": _("Customer"),
                },
            ]
        },
    ]

# Custom API Endpoints
api_version = 1

api_routes = {
    "POST /api/method/customer_app.customer_app.api.customer_api.create_customer": "customer_app.api.customer_api.create_customer",
    "GET /api/method/customer_app.api.customer_api.get_customers": "customer_app.api.customer_api.get_customers"
}