# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    driver_id = fields.Many2one('res.partner', string='Driver',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},)
