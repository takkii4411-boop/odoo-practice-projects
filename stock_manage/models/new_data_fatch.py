from odoo import models, fields, api

class CigaretteStockLines(models.Model):
    _name = 'cigarette.stock.lines'
    _description = 'Cigarette Details Table'

    report_id = fields.Many2one('cigarette.stock.report', ondelete='cascade')
    brand_name = fields.Char(string="Brand Name")
    quantity = fields.Float(string="Quantity", digits=(16, 2))