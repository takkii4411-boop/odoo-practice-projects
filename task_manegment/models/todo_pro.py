from odoo import fields, models, api


class TodoPro(models.Model):
    _name = 'todo.pro'
    _description = 'todo data manege'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date')
    description = fields.Char(string='Description')

    task_order = fields.Char(
        string='Task Unique Code',
        readonly=True,
        copy=False,
        default='New',
        tracking=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('task_order', 'New') == 'New' or not vals.get('task_order'):
                vals['task_order'] = self.env['ir.sequence'].next_by_code('todo.order') or 'New'
        return super().create(vals_list)
