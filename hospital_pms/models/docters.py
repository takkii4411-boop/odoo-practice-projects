from odoo import models, fields, api


class Docter(models.Model):
    _name = 'hospital.docters'
    _description = 'Hospital Docter'

    _rec_name = 'rec_docters'
    _description = 'docter name with category'

    name = fields.Char(string="Docter Name", required=True)
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], required=True)
    contact = fields.Char(string="Contact", size=(10), required=True)
    collage = fields.Char(string="Collage Name", required=True)
    digree = fields.Char(string="Qualification Digree", required=True)
    mark = fields.Float(string="Mark In Persent", digits=(3, 2), required=True)
    masters_id = fields.Many2one('spacle.categorys', string="Select Value", required=True)
    priview = fields.Boolean(string='Priview Image', default=False)
    docters_sequence = fields.Char(invisible=True, readonly=True, copy=False)
    rec_docters = fields.Char(string="Record Identity", compute="_compute_name_category", store=True)
    image_1920 = fields.Image(string="Upload Photo", required=True,
                              help="Click on the image or the pencil icon to upload a new photo")
    specialty_categorys = fields.Selection([('general', 'General'), ('heart_lungs', 'Heart & Lungs'),
                                            ('brain_nerves', 'Brain & Nerves'),
                                            ('women_children', 'Women & Children'),
                                            ('skin_eye_ent', 'Skin / Eye / ENT'),
                                            ('surgery', 'Surgery'),
                                            ('internal_organs', 'Internal Organs'),
                                            ('cancer_blood', 'Cancer & Blood'),
                                            ('checkup', 'Checkup'),
                                            ('test', 'Lab Test'),
                                            ],
                                           string="Specialty Category", required=True)

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
            if vals.get('docters_sequence', 'new') == 'new':
                vals['docters_sequence'] = self.env['ir.sequence'].next_by_code('docters.seq.order') or 'new'
        return super().create(vals_list)

    active = fields.Boolean('Active', default=True)
    status_text = fields.Selection([
        ('active', 'On-Duty'),
        ('inactive', 'Off-Duty'),
    ], string="Status", compute="_compute_status_text")

    @api.depends('active')
    def _compute_status_text(self):
        for record in self:
            record.status_text = 'active' if record.active else 'inactive'


    @api.depends('name', 'masters_id')
    def _compute_name_category(self):
        for record in self:
            name = record.name or ""
            cat = record.masters_id.name if record.masters_id else ""
            record.rec_docters = f"{name} [{cat}]"
