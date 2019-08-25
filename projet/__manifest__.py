# -*- coding: utf-8 -*-
{
    'name': "projet",

    'summary': """
        Request materiel""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'stock', 'account', 'purchase', 'sale_management', 'hr_holidays', 'project', 'hr_timesheet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/personne_views.xml',
        'views/employe_views.xml',
        'views/conges_views.xml',
        'views/inventaire_views.xml',
        'views/feuille_de_temps_views.xml',
        'views/ventes_views.xml',
        'views/achats_views.xml',
        'views/projets_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': False,
    'licence': 'AGPL-3',
    'qweb': [],
}