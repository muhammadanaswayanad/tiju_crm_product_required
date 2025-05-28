from odoo import fields, models

class CrmStage(models.Model):
    _inherit = 'crm.stage'

    mandatory_field_configs = fields.One2many(
        'crm.stage.mandatory.field',
        'stage_id',
        string="Mandatory Fields for this Stage",
        help="Configure fields that must be filled when an opportunity is in this stage."
    )
