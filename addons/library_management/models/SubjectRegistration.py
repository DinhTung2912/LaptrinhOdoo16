from odoo import models, fields, api
from odoo.exceptions import UserError

class SubjectRegistration(models.Model):
    _name = 'library.subject.registration'
    _description = 'Subject Registration'

    name = fields.Char(string="Subject Registration")
    student_id = fields.Many2one('library.student', string='Student')
    subject_id = fields.Many2one('library.subject', string='Subject')



