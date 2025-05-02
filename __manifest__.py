{
    'name': 'Tiju CRM Product Required',
    'version': '17.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Makes the product/course field required in specific CRM stages',
    'description': """
        This module makes the product_id field (Course) required in the CRM lead form,
        but only in certain stages:
        - Not Interested (NI)
        - Neutral Prospect (NP)
        - Future Prospect (FP)
        - Prospect (P)
        - Hot Prospect (HP)
        - Admission (A)
        - LOST
    """,
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
