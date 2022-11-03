# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    transporter_id = fields.Many2one('res.partner', string='Transporter', )
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
