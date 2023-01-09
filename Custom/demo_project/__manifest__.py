# -*- coding: utf-8 -*-
{
    'name': 'Demo Project',
    'summary': """Something about the App.""",
    'description': """
App Name
========
Something about the App.
    """,
    'version': '15.0.1.0',
    'author': 'Company Name',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'web',
    ],
    'data': [
        ## Security
        'security/ir.model.access.csv',

        ## View
        'views/student.xml',
        'views/menus.xml',
    ],
    # 'qweb': [
    #     ## Template
    #     'static/src/xml/*.xml',
    # ],

    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
    ],
}
