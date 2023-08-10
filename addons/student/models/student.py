from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')