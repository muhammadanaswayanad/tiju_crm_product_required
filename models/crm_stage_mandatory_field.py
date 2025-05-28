from odoo import fields, models, api

class CrmStageMandatoryField(models.Model):
    _name = 'crm.stage.mandatory.field'
    _description = 'CRM Stage Mandatory Field Configuration'
    _order = 'stage_id, sequence, id'

    sequence = fields.Integer(default=10)
    stage_id = fields.Many2one('crm.stage', string='Stage', required=True, ondelete='cascade')
    field_id = fields.Many2one(
        'ir.model.fields',
        string='Field',
        required=True,
        domain="[('model_id.model', '=', 'crm.lead'), ('store', '=', True), "
               "('ttype', 'not in', ['one2many', 'many2many', 'binary', 'reference', 'function']), "
               "('name', '!=', 'stage_id')]",  # Avoid making stage_id mandatory via this config
        help="Select a field from the Lead/Opportunity model that should be mandatory for this stage."
    )
    field_technical_name = fields.Char(related='field_id.name', string="Technical Name", readonly=True, store=True)

    _sql_constraints = [
        ('stage_field_uniq', 'unique(stage_id, field_id)', 'A field can only be configured once per stage.')
    ]

    @api.constrains('field_id')
    def _check_field_is_not_stage_id(self):
        for record in self:
            if record.field_id and record.field_id.name == 'stage_id':
                raise models.ValidationError("The 'Stage' field itself cannot be selected as a mandatory field through this configuration.")

```
