from odoo import models, fields, api


class CustomProjectTask(models.Model):
    _inherit = 'project.task'

    duration = fields.Integer(string='Duration (days)', related='stage_id.duration')
    remain_days = fields.Integer(string='Remaining Days', compute='_compute_remain_days')
    start_date = fields.Date(string='Start Date')
    stage_id = fields.Many2one('project.task.type', string='Stage')
    history_ids = fields.One2many('task.history', 'task_id', string='Task History')
    state = fields.Selection([
        ('late', 'Trễ'),
        ('on_time', 'Đúng tiến độ'),
        ('early', 'Sớm tiến độ')
    ], string='Trạng thái', compute='_compute_state')

    @api.depends('start_date', 'duration', 'stage_id')
    def _compute_remain_days(self):
        for task in self:
            if task.start_date and task.duration:
                today = fields.Date.today()
                delta = task.start_date - today
                task.remain_days = max(0, delta.days)
            else:
                task.remain_days = 0

    @api.depends('start_date', 'duration', 'stage_id')
    def _compute_state(self):
        for task in self:
            if task.start_date and task.duration:
                today = fields.Date.today()
                delta = task.start_date - today
                if delta.days > task.duration:
                    task.state = 'late'
                elif delta.days == task.duration:
                    task.state = 'on_time'
                else:
                    task.state = 'early'
            else:
                task.state = 'late'

    @api.onchange('stage_id')
    def _onchange_stage_id(self):

        if self.stage_id:
            previous_stage_id = self._origin.stage_id if self._origin else False

            if previous_stage_id and self.stage_id != previous_stage_id:
                history_vals = {
                    'task_id': self.id,
                    'stage_id': previous_stage_id.id,
                    'start_date': self.start_date,
                    'end_date': fields.Date.today(),
                }
                self.env['task.history'].create(history_vals)

        self.start_date = self.date_assign
