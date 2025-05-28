from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    def _check_stage_mandatory_fields(self):
        for lead in self:
            if not lead.stage_id or not lead.stage_id.mandatory_field_configs:
                continue
            
            missing_fields = []
            for config in lead.stage_id.mandatory_field_configs:
                field_name = config.field_technical_name
                if not lead[field_name]: # Checks for falsy values (False, None, 0, empty string/list)
                    # For boolean fields, if False is a valid "filled" state, this logic might need adjustment
                    # or the field shouldn't be marked mandatory if False is acceptable.
                    # Typically, mandatory boolean means it must be True.
                    field_label = lead.fields_get([field_name])[field_name]['string']
                    missing_fields.append(field_label)
            
            if missing_fields:
                error_message = _("The following fields are mandatory for stage '%(stage_name)s':\n- %(fields_list)s") % {
                    'stage_name': lead.stage_id.name,
                    'fields_list': "\n- ".join(missing_fields)
                }
                raise ValidationError(error_message)

    @api.model_create_multi
    def create(self, vals_list):
        leads = super().create(vals_list)
        for lead in leads:
            # Ensure stage_id is loaded if it was part of vals or defaults
            if 'stage_id' in vals_list[0] or lead.stage_id: # Check first vals for stage_id presence
                 lead._check_stage_mandatory_fields()
        return leads

    def write(self, vals):
        res = super().write(vals)
        # Check either if stage changed or if any other field that might be mandatory is being written
        # For simplicity, always check after a write if stage_id is set.
        for lead in self:
            if lead.stage_id: # Only check if there's a stage
                lead._check_stage_mandatory_fields()
        return res
