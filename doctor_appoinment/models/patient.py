from odoo import api,models,fields

class InheritPatient(models.Model):
    _inherit = 'hospital.patient'
    _description = 'InheritPatient'

    appointment_ids = fields.One2many('hospital.appointment','patient_id',string='appointment')
    appointment_count = fields.Integer(compute='_appointment_count' , store=True)



    @api.depends('appointment_ids')
    def _appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    def action_view_appointments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'domain': [('patient_id', '=', self.id)],
            'context': {'default_patient_id': self.id}

        }