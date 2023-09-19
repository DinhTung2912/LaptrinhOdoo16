from odoo import models, fields, api


class TaskHistory(models.Model):
    _name = 'task.history'
    _description = 'Task History'

    task_id = fields.Many2one('project.task', string='Task')
    stage_id = fields.Many2one('project.task.type', string='Stage',readonly=True)
    start_date = fields.Date(string='Start Date', readonly=True)
    end_date = fields.Date(string='End Date', readonly=True)
    state = fields.Selection([
        ('completed', 'Đã hoàn thành'),
        ('incomplete', 'Chưa hoàn thành'),
    ], string='State', compute='_compute_state')

    @api.depends('start_date', 'end_date')
    def _compute_state(self):

        for history in self:
            if history.start_date and history.end_date:
                if history.end_date > history.start_date:
                    history.state = 'completed'
                else:
                    history.state = 'incomplete'
            else:
                history.state = False
