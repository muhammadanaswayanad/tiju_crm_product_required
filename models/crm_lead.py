from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    course_id = fields.Many2one('product.product', string='Course', 
        domain="[('type', '=', 'service')]",
        help="Select the course related to this opportunity")
