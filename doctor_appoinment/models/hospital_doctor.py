from datetime import date
from odoo import fields, models, api


class HospitalDocter(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _rec_name = 'rec_doctor'

    name = fields.Char(string="Docter Name", required=True)
    doctor_seq = fields.Char(invisible=True, readonly=True, copy=False)
    rec_doctor = fields.Char(string="Record Identity", compute="_compute_name_category", store=True)
    respect_name = fields.Char(string="Respect Name", compute="_compute_respect_name", store=True)
    dr = fields.Char(default='Dr.')
    specialization = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('general_medicine', 'General Medicine'), ], string='Specialization', required=True)
    contact = fields.Char(string="Contact", size=(10), required=True)
    email = fields.Char(string='Email', required=True)
    consultation_fee = fields.Float(string="Consultation Fee", digits=(16, 2))
    experience_years = fields.Integer(string="Experience Years", required=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string=' Age', compute='_compute_age', readonly=True, store=True)
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], required=True)
    image = fields.Binary(string='Upload Photo', required=True)
    priview = fields.Boolean(string='Priview Image', default=False)
    appointment_id = fields.One2many('hospital.appointment', 'doctor_id', string='Appointment')
    appointment_count = fields.Integer(compute='_compute_appointment_count', store=True)
    place = fields.Selection([('andhra_pradesh', 'Andhra Pradesh'),
                              ('arunachal_pradesh', 'Arunachal Pradesh'),
                              ('assam', 'Assam'),
                              ('bihar', 'Bihar'),
                              ('chhattisgarh', 'Chhattisgarh'),
                              ('goa', 'Goa'),
                              ('gujarat', 'Gujarat'),
                              ('haryana', 'Haryana'),
                              ('himachal_pradesh', 'Himachal Pradesh'),
                              ('jharkhand', 'Jharkhand'),
                              ('karnataka', 'Karnataka'),
                              ('kerala', 'Kerala'),
                              ('madhya_pradesh', 'Madhya Pradesh'),
                              ('maharashtra', 'Maharashtra'),
                              ('manipur', 'Manipur'),
                              ('meghalaya', 'Meghalaya'),
                              ('mizoram', 'Mizoram'),
                              ('nagaland', 'Nagaland'),
                              ('odisha', 'Odisha'),
                              ('punjab', 'Punjab'),
                              ('rajasthan', 'Rajasthan'),
                              ('sikkim', 'Sikkim'),
                              ('tamil_nadu', 'Tamil Nadu'),
                              ('telangana', 'Telangana'),
                              ('tripura', 'Tripura'),
                              ('uttar_pradesh', 'Uttar Pradesh'),
                              ('uttarakhand', 'Uttarakhand'),
                              ('west_bengal', 'West Bengal'), ], string="Place", required=True, )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('doctor_seq', 'new') == 'new':
                vals['doctor_seq'] = self.env['ir.sequence'].next_by_code('doctor.sequence') or 'new'
        return super().create(vals_list)

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                rec.age = date.today().year - rec.dob.year
            else:
                rec.age = 0

    @api.depends('name', 'specialization')
    def _compute_name_category(self):
        for record in self:
            name = record.name or ""
            cat = record.specialization if record.specialization else ""
            record.rec_doctor = f"{name} [{cat}]"

    @api.depends('appointment_id')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_id)

    @api.depends('name', 'dr')
    def _compute_respect_name(self):
        for record in self:
            name = record.name or ""
            cat = record.dr if record.dr else ""
            record.respect_name = f"{cat}{name}"

    def action_view_appointments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'domain': [('doctor_id', '=', self.id)],
            'context': {'default_doctor_id': self.id}

        }


    def get_all_docs_method(self):
        all_docs_ids = self.env['hospital.doctor'].search([])
        return all_docs_ids
