# -*- coding: utf-8 -*- 


{
    'name': 'Transfers transportation infos',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.3',
    'category': 'Stock',
    'demo': [],
    'depends': ['fleet','stock'],
    'data': [
        'security/stock_picking_transportation_info_security.xml',
        'views/stock_picking_views.xml',
        'report/report_deliveryslip.xml'
    ],
    'license': 'LGPL-3',
}
