# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sale Order Report Discount Total Reorder",
    "summary": "Reorders discount totals in Sale order reports.",
    "version": "17.0.1.0.0",
    "category": "Accounting",
    "website": "https://github.com/sygel-technology/sy-sale-reporting",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale_discount_display_amount",
    ],
    "data": [
        "report/sale_order_templates.xml",
    ],
}
