# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class MaintenanceModel(models.Model):
    _name = 'odoo_view_advanced.maintenance_model'

    client = fields.Many2one("res.partner",string='Name')
    category = fields.Many2one("odoo_view_advanced.category_model",string="Product")
    subcategory = fields.Many2one("odoo_view_advanced.subcategory_model",string="Item")
    rating = fields.Integer(default=0,string='Rating')



    @api.onchange('category')
    def onchange_category(self):
            self.subcategory = ""
            domain = {'subcategory': [('category_id', '=', self.category.id)]}
            return {'domain': domain}
            