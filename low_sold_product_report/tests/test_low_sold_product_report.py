# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import datetime

from odoo.tests import TransactionCase


class TestLowSoldProductReport(TransactionCase):
    def setUp(cls, *args, **kwargs):
        # Created data can't be queried in reports
        # because the database registry is not updated in tests.
        # See sale module demo data
        super().setUp()

    def test_low_sold_product_report(self):
        ctx = {
            "product_type": "product_product",
            "date_from": datetime.date.today(),
            "date_to": datetime.date.today() + datetime.timedelta(days=1),
            "sold_quantity_limit": 1,
            "sold_amount_limit": 0,
        }
        report_lines = (
            self.env["low.sold.product.report"].sudo().with_context(**ctx).search([])
        )
        self.assertEqual(len(report_lines), 2)
        self.assertEqual(
            report_lines.mapped("product_id"),
            (
                self.env.ref("product.consu_delivery_01")
                | self.env.ref("product.product_product_4")
            ),
        )
        self.assertEqual(report_lines[:1].product_uom_qty, 1)
