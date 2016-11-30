# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class TipoPrenda(models.Model):
    _name = 'com.camilasport.tipo.prenda'

    codigo = fields.Char(string="Codigo",)
    nombre = fields.Char(string="Nombre del tipo de prenda", required=True)
