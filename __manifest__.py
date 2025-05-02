{
    'name': 'CRM Product/Course Required',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Make Course field required in CRM',
    'description': """
        This module makes the course field required in CRM leads/opportunities.
    """,
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
