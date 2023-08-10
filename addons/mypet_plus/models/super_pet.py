from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class SuperPet(models.Model):
    _name = "super.pet"
    _inherit = "my.pet"
    _description = "Prototype inheritance"

    # add new fieldn
    is_super_strength = fields.Boolean("Is Super Strength", default=False)
    is_fly = fields.Boolean("Is Super Strength", default=False)
    planet = fields.Char("Planet")

    # avoid erroe: TypeError : Many2 many fields super.pet.product_ids and my.pet.product_ids use the same table
    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                   relation='super_pet_product_rel',
                                   column1='col_pet_id',
                                   column2='col_product_id')
