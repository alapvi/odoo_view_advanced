# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class SubcategoryModel(models.Model):
    _name = 'odoo_view_advanced.subcategory_model'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    category_id = fields.Many2one("odoo_view_advanced.category_model",string="Category")
    

