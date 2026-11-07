{
    'name': 'Hospital Management',
    'version': '1.0',
    'license': "LGPL-3",
    'description': """ on this module Hospital PMS allows you to save patients recodes """,
    'sequence': 1,
    'author': 'By..Rajan',
    'category': 'Services',
    'summary': 'Hospital Management System Odoo Practice Project',
    'depends': ['base', ],
    'data': [
        # XML views, menus, security, etc.
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_views.xml',
        'reports/paperformat.xml',
        'reports/patient_reports.xml',
        'reports/reports.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'patient_management/static/src/scss/patient_style.scss',
        ], },
    'sequence': 1,
    'installable': True,
    'application': True,
}
