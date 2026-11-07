from odoo import fields, models, api

class Reminder(models.TransientModel):
    _name = 'reminder.wizard'
    _description = 'Reminder For Delete Detail In Appointment'

    appointment_id = fields.Many2one('hospital.appointment',invisible=True, readonly=True, copy=False)
    patient_age = fields.Integer(related='appointment_id.patient_age')
    appointment_seq = fields.Char(related='appointment_id.name')
    patient_name = fields.Char(related='appointment_id.respect_patient_name')


    def cancel_button_wizard(self):
        recent_rec = self.env.context.get('active_id') #remamber the record what is open on that time
        rec_allData = self.env['hospital.appointment'].browse(recent_rec) # carry all record of the record
        if rec_allData:
            rec_allData.stage = 'cancel'
