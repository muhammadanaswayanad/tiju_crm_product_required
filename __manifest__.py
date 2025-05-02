{
    'name': 'CRM Course Required by Stage',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Make Course field required based on CRM stage',
    'description': """
        This module allows users to configure which CRM stages require a course field,
        without needing code changes.
    """,
    'depends': ['crm', 'product'],
    'data': [
        'views/crm_stage_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
