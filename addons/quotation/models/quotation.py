from odoo import models, fields, api


class Quotation(models.Model):
    _inherit = 'sale.order'
    _name = 'sale.order'
    item_discount_percent = fields.Float(string='Item Discount %', help='Discount percentage for each item')
    discount_amount = fields.Monetary(string='Discount Amount', compute='_compute_discount_amount')
    grand_total = fields.Monetary(string='Grand Total', compute='_compute_grand_total')

    @api.depends('item_discount_percent', 'amount_total')
    def _compute_discount_amount(self):
        for order in self:
            order.discount_amount = order.item_discount_percent / 100 * order.amount_total

    @api.depends('amount_total', 'discount_amount')
    def _compute_grand_total(self):
        for order in self:
            order.grand_total = order.amount_total - order.discount_amount
