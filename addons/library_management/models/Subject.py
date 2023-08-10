# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class Subjects(models.Model):
    _name = "library.subject"
    _description = "Subjects"

    name = fields.Char(string="Subjects Name", required=True)

