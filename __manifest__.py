# -*- coding: utf-8 -*-
{
    'name': "immobilier",

    'summary': """
         Gestion des activités immobiliere""",

    'description': """
        Gestion des activites immobilieres
        - Gestion des ventes
        - Gestion des locations
    """,

    'author': "HSN Consult",
    'website': "https://www.www.hsnconsult.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/immobilier_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
