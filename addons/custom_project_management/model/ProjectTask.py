from odoo import models, fields, api


class CustomProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    duration = fields.Integer(string='Duration (days)')
