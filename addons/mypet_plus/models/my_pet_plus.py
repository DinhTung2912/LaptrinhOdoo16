from odoo import api, fields, models, tools
from odoo.exceptions import UserError, ValidationError


class MyPetPlus(models.Model):
    _name = "my.pet"
    _inherit = "my.pet"
    _description = "Extend mypet models"

    # add new file
    toy = fields.Char('Pet Toy', required=False)

    # modify  old field
    age = fields.Integer('Pet Age', default=2)  # chat default age from 1 to 2
    gender = fields.Selection(selection_add=[('sterilizattion', 'Sterilization')])
