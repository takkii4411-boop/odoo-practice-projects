{
    'name': 'TO-DO MANEGER',
    'version': '1.0',
    'license': "LGPL-3",
    'description': """ on this module track & recodes your day to day task and mantaine it""",
    'sequence': 1,
    'author': 'By..Rajan',
    'category': 'Services',
    'summary': 'TRACK YOUR TASK AND MANAGE IT',
    'depends': ['base', 'website_sale','portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'data/sequence.xml',
        'web_views/web_icon.xml',
        'web_views/portal_pet_templates.xml',
        'web_views/portal_pet_create.xml',
        'views/todo-views.xml',
    ],

    # 'assets': {
    #     'web.assets_backend': [
    #
    #     ], },

    'installable': True,
    'application': True,
}
