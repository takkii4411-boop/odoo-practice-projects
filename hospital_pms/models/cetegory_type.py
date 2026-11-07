from odoo import models, fields


class SpeciltyCategory(models.Model):
    _name = 'sp.category'
    _description = 'Master Data for spacle category'

    name = fields.Char(string="Value")
    datatype = fields.Selection([
        ('general', 'General'),
        ('heart_lungs', 'Heart & Lungs'),
        ('brain_nerves', 'Brain & Nerves'),
        ('women_children', 'Women & Children'),
        ('skin_eye_ent', 'Skin / Eye / ENT'),
        ('surgery', 'Surgery'),
        ('internal_organs', 'Internal Organs'),
        ('bones_muscles', 'Bones & Muscles'),
        ('cancer_blood', 'Cancer & Blood'),
        ('emergency_others', 'Emergency & Others'),
        ('checkup', 'Checkup'),
        ('test', 'Lab Test'),
    ], string="Category")

class SpeciltyCategory(models.Model):
    _name = 'spacle.categorys'
    _description = 'Master Data for spacle categorys'

    name = fields.Char(string="Value")
    data_types = fields.Selection([
        ('general', 'General'),
        ('heart_lungs', 'Heart & Lungs'),
        ('brain_nerves', 'Brain & Nerves'),
        ('women_children', 'Women & Children'),
        ('skin_eye_ent', 'Skin / Eye / ENT'),
        ('surgery', 'Surgery'),
        ('internal_organs', 'Internal Organs'),
        ('bones_muscles', 'Bones & Muscles'),
        ('cancer_blood', 'Cancer & Blood'),
        ('emergency_others', 'Emergency & Others'),
        ('checkup', 'Checkup'),
        ('test', 'Lab Test'),
    ], string="Category")


