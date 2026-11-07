from email.policy import default

from odoo import models, fields,api


class Patient(models.Model):
    _name = 'hospital.patients'
    _description = 'Hospital Patient'

    _rec_name = 'rec_patients'
    _description = 'Hospital Patient Record'

    name = fields.Char(string="Patient Name", required=True)
    dob = fields.Date(string="Date of birth", required=True)
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], required=True)
    phone_number = fields.Char(string="Phone Number", size=(10), required=True)
    category_filter = fields.Selection([
        ('general', 'General'),
        ('heart_lungs', 'Heart & Lungs'),
        ('brain_nerves', 'Brain & Nerves'),
        ('women_children', 'Women & Children'),
        ('skin_eye_ent', 'Skin / Eye / ENT'),
        ('internal_organs', 'Internal Organs'),
        ('cancer_blood', 'Cancer & Blood'),
        ('checkup', 'Checkup'),
        ('test', 'Lab Test'),
    ], string="Disease Type", required=True)
    master_ids = fields.Many2one('sp.category', string="Problem", required=True)
    image_1920 = fields.Image(string="Upload Your Photo", )
    priview = fields.Boolean(string='Priview Image', default=False)
    sequence_patients =fields.Char(string="Patients_Order",)

    rec_patients = fields.Char(string="Record Identity", compute="_compute_name_category", store=True)

    @api.depends('name', 'master_ids')
    def _compute_name_category(self):
        for record in self:
            name = record.name or ""
            cat = record.master_ids.name if record.master_ids else ""
            record.rec_patients = f"{name} [{cat}]"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sequence_patients', 'new') == 'new':
                vals['sequence_patients'] = self.env['ir.sequence'].next_by_code('patients.seq.order') or 'new'

        return super().create(vals_list)

    active = fields.Boolean('Active', default=True)
    status_text = fields.Selection([
        ('active', '● Treatment On'),
        ('inactive', '○ DisCharge')
    ], string="Status", compute="_compute_status_text")

    @api.depends('active')
    def _compute_status_text(self):
        for record in self:
            record.status_text = 'active' if record.active else 'inactive'
