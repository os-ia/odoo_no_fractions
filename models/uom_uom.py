# -*- coding: utf-8 -*-

from odoo import models, fields


class UoMCategory(models.Model):
    _inherit = 'uom.category'

    avoid_sell_fractions = fields.Boolean('Avoid Sell Fractions', default=False)
