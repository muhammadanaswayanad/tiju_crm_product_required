{
    'name': 'CRM Dynamic Mandatory Fields by Stage',
    'version': '17.0.1.0.0', # Updated version for Odoo 17 and new features
    'category': 'Sales/CRM',
    'summary': 'Configure specific fields on Leads/Opportunities to be mandatory based on CRM stage.',
    'description': """
        This module enhances Odoo's CRM by allowing administrators to define
        which fields on a Lead/Opportunity become mandatory when it reaches a specific stage.

        Features:
        - Configure mandatory fields per CRM stage via the stage form.
        - Select any storable field from crm.lead to be conditionally mandatory.
        - Validation prevents saving an opportunity if mandatory fields for its current stage are not filled.
        - Flexible and does not require code changes to add new mandatory field rules once installed.
    """,
    'author': 'Tiju', # Assuming you are Tiju, or update as needed
    'depends': ['crm', 'sales_team'], # sales_team for group_sale_manager
    'data': [
        'security/ir.model.access.csv',
        'views/crm_stage_views.xml',
        'views/crm_lead_views.xml', # Kept for structure, though content is commented out
        # Add views for crm_stage_mandatory_field if a separate menu item is desired,
        # but for now, it's managed through the crm.stage form.
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
