# File: models/employee_department.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class EmployeeDepartment(models.Model):
    _inherit = 'hr.department'

    # Bổ sung trường one2many member_ids vào model hr.department
    member_ids = fields.One2many('hr.employee', 'department_id', string='Members')


