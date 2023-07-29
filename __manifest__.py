# __manifest__.py

{
    'name': 'Material Management',
    'version': '1.0',
    'summary': 'Module for managing materials and suppliers',
    'description': """
        This module allows users to manage materials that will be sold. 
        It includes information such as Material Code, Material Name, Material Type, Material Buy Price, and Related Supplier.
    """,
    'category': 'Sales',
    'author': 'Ahmad Nursidik Dinar',
    'depends': ['base'],
    'data': [
        'views/material_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
