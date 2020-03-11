# -*- coding: utf-8 -*-
{
    'name': "{{ jonathan }}",

    'summary': """
        creacion de campos productos terminados""",

    'description': """
        seis campos para productos terminados
    """,

    'author': "Todoo",
    'website': "http://www.todoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productos',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'view/campos_view.xml',
        
    ],
    # only loaded in demonstration mode
    'application': True,
}

