from odoo import models, fields


class Student(models.Model):
    _name = 'library.student'
    _description = 'Student Information'

    name = fields.Char('Name', required=True)
    student_id = fields.Char('Student ID', required=True)
    age = fields.Integer('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    subject_ids = fields.One2many('library.subject.registration', 'student_id', string='Subject Registration')