{
    'name': "Stock Manage System SMS",
    'version': '19.0.1.1',
    'license': "LGPL-3",
    'description': """ save and store recode of stock of material """,
    'author': "By Rajan",
    'category': 'Record And Stock Management',
    'sequence': 1,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/data_fatch_form_views.xml',
        'views/action.xml',

    ],
    'installable': True,
    'application': True,
}
