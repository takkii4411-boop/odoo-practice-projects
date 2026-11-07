from odoo import api, models, fields


class HospitalAppoinmnt(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appoinment'

    name = fields.Char(invisible=True, readonly=True, copy=False, defult="new")
    patient_id = fields.Many2one('hospital.patient', string='Patient name', required=True, ondelete='cascade')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor name', required=True)
    appointment_date = fields.Date(string='Appoin on', copy=False)
    appointment_time = fields.Selection([
        ('9:00am', '9:00 AM'),
        ('10:00am', '10:00 AM'),
        ('11:00am', '11:00 AM'),
        ('2:00pm', '2:00 PM'),
        ('3:00pm', '3:00 PM'),
        ('4:00pm', '4:00 PM'), ], string='Time Slot', required=True)
    stage = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'), ], default='draft')
    reason = fields.Text(string='Reason for Visit', copy=False)
    notes = fields.Text(string='Additional Notes', copy=False)
    patient_age = fields.Integer(string='Patient Age', related='patient_id.age', copy=False)
    patient_ids = fields.Char(related='patient_id.patient_seq')
    respect_patient_name = fields.Char(string='patient Name ', related='patient_id.name')
    doctor_fee = fields.Float(string='Fee', related='doctor_id.consultation_fee', copy=False)
    doc_respect_name = fields.Char(string='Doctor Name ', related='doctor_id.respect_name')
    doctor_ids = fields.Char(related='doctor_id.doctor_seq')
    specialization = fields.Char(string='Specialization Name', compute='_compute_specialization_label')

    @api.depends('doctor_id.specialization')
    def _compute_specialization_label(self):
        for rec in self:
            label = ''
            if rec.doctor_id.specialization:
                selection_dict = dict(rec.doctor_id._fields['specialization'].selection)
                label = selection_dict.get(rec.doctor_id.specialization, '')
            rec.specialization = label

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'new') == 'new':
                vals['name'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or 'new'
        return super().create(vals_list)

    def action_draft(self):
        for rec in self:
            rec.stage = 'draft'

    def action_confirmed(self):
        for rec in self:
            rec.stage = 'confirmed'

    def action_done(self):
        for rec in self:
            rec.stage = 'done'

    def action_cancel(self):
        for rec in self:
            rec.stage = 'cancel'

    def cancel_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Remar cancel',
            'res_model': 'reminder.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
            'default_appointment_id': self.id,
            },
        }
