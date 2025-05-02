from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    course_id = fields.Many2one('product.product', string='Course', 
        domain="[('type', '=', 'service')]",
        help="Select the course related to this opportunity")
        
    @api.onchange('stage_id')
    def _onchange_stage_id_for_course_required(self):
        if self.stage_id and self.stage_id.course_required:
            self = self.with_context(enforce_course_required=True)
        else:
            self = self.with_context(enforce_course_required=False)
            
    @api.constrains('stage_id', 'course_id')
    def _check_course_required(self):
        for record in self:
            if record.stage_id and record.stage_id.course_required and not record.course_id:
                raise ValidationError(_("A course must be selected for opportunities in the '%s' stage.") % record.stage_id.name)
