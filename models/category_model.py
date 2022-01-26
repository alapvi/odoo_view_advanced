# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class CategoryItem(models.Model):
    _name = 'odoo_view_advanced.category_model'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    subcategory_ids = fields.One2many("odoo_view_advanced.subcategory_model","category_id",string="Subcategory")
    

