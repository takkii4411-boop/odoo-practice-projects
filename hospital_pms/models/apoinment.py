from odoo import models, fields, api

class Apoinment(models.Model):
    _name = 'hospital.apoinment'
    _description = 'Hospital Apoinment'

    name = fields.Char(string="Value")
    docters_rec = fields.Many2one('hospital.docters',string="Dr.")
    docters_pic = fields.Image(string="Docters Identity", related='docters_rec.image_1920')
    patient_rec = fields.Many2one('hospital.patients',string="Patient")
    apoin = fields.Datetime(string="Apointed Date")
    patients_pic = fields.Image(string="Patients Identity")
    patients_pic = fields.Image(string="Patients Identity", related='patient_rec.image_1920')
    apoin_order = fields.Char(invisible=True, readonly=True, copy=False, default='New')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('apoin_order', 'new') == 'new':
                vals['apoin_order'] = self.env['ir.sequence'].next_by_code('apoinment.seq.order') or 'new'
        return super().create(vals_list)
