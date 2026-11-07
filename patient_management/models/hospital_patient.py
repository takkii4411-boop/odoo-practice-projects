from odoo import fields, models, api
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'HospitalPatient'
    _rec_name = 'rec_patients'

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string=' Age', compute='_compute_age', readonly=True , store=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    priview = fields.Boolean(string='Priview Image', default=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    rec_patients = fields.Char(string="Record Identity", compute="_compute_name_category", store=True)
    blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'),
                                    ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB_')])
    problem = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('general_medicine', 'General Medicine'), ], string='Disease', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    email = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address', required=True)
    image = fields.Binary(string='Upload Photo', required=True)
    patient_seq = fields.Char(string='Patient Sequence', )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('patient_seq', 'new') == 'new':
                vals['patient_seq'] = self.env['ir.sequence'].next_by_code('patient.sequence') or 'new'
        return super().create(vals_list)

    @api.depends('name', 'problem')
    def _compute_name_category(self):
        for record in self:
            name = record.name or ""
            cat = record.problem if record.problem else ""
            record.rec_patients = f"{name} ({cat})"

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = date.today().year - rec.date_of_birth.year
            else:
                rec.age = 0

