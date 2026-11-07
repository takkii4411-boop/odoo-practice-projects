{
    'name': 'Hospital Management Doctor',
    'version': '1.0',
    'license': "LGPL-3",
    'description': """ on this module Hospital PMS allows you to save patients recodes """,
    'sequence': 1,
    'author': 'By..Rajan',
    'category': 'Services',
    'summary': 'Hospital Management System Odoo Practice Project',
    'depends': ['base', 'patient_management'],
    'data': [
        # XML views, menus, security, etc.
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/appointment_views.xml',
        'views/inheritpatient_views.xml',
        'views/doctor_views.xml',
        'wizard/wizard_views.xml',
        'reports/paperformat.xml',
        'reports/appointment_reports.xml',
        'reports/doctor_report.xml',
        "reports/reports.xml",


    ],
    'assets': {
        'web.assets_backend': [
            'doctor_appoinment/static/src/scss/docter_style.scss',
        ], },
    'sequence': 1,
    'installable': True,
    'application': True,
}
