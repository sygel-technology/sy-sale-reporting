import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-sale-reporting",
    description="Meta package for sygel-technology-sy-sale-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-so_product_set_report_hide_lines>=15.0dev,<15.1dev',
        'odoo-addon-so_report_hide_lines>=15.0dev,<15.1dev',
        'odoo-addon-so_report_hide_price>=15.0dev,<15.1dev',
        'odoo-addon-so_report_hide_price_portal>=15.0dev,<15.1dev',
        'odoo-addon-so_report_hide_salesperson>=15.0dev,<15.1dev',
        'odoo-addon-so_report_only_date>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
