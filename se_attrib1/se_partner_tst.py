# -*- coding: utf-8 -*-
from openerp import models, fields, api
class se_attribute(models.Model):
#   
    _inherit = 'product.category'
    ef_grpt = fields.Integer('Группа продукта')
#   
    _inherit = 'product.category'
    ef_kat_vidt = fields.Integer('Категория продукта')
#   
    _inherit = 'product.category'
    ef_kat_vidt_kat_grpt_kod = fields.Integer('Родительская категория продукта')
#   
    _inherit = 'product.template'
    ef_id = fields.Integer('Код продукта из ЛО')
#   
    _inherit = 'product.product'
    ef_id_ = fields.Integer('Код продукта из ЛО')

