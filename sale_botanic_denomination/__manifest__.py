# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Botanic Denomination",
    "summary": "Adds the botanic denomination to menus and sale report's products",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "website": "https://github.com/sygel-technology/sy-sale-reporting",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product_botanic_denomination",
        "sale_management",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/botanic_denomination_views.xml",
    ],
}
