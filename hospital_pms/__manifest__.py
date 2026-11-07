{
    'name': "Hospital PMS",
    'version': '18.0.1.1',
    'license': "LGPL-3",
    'description': """ on this module Hospital PMS allows you to save patients recodes """,
    'author': "By Rajan",
    'category': 'HMS-Patients & Docters Manegment System',
    'sequence': 1,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/apoinment.xml',
        'sequence/sequence.xml',
        'master_data/patient_master_data.xml',
        "master_data/docter_master_data.xml",
        "views/patients_record_views.xml",
        "views/docters_record_views.xml"
    ],
    'installable': True,
    'application': True,
}
