from odoo import fields, models

class CrmStage(models.Model):
    _inherit = 'crm.stage'

    course_required = fields.Boolean(string="Course Mandatory in this Stage?", default=False,
                                     help="If checked, the course field will be required for leads in this stage")
