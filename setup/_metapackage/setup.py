import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-sale-reporting",
    description="Meta package for sygel-technology-sy-sale-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-sale_order_report_hide_discounts_by_partner>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
