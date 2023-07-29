# material.py

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material'
    _description = 'Material'

    name = fields.Char(string='Material Name', required=True)
    code = fields.Char(string='Material Code', required=True)
    type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], string='Material Type', required=True)
    buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('supplier', string='Related Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for material in self:
            if material.buy_price < 100:
                raise ValidationError("Material buy price must be greater than or equal to 100.")

