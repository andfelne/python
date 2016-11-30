# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class Medidas(models.Model):
    _name = 'com.camilasport.medidas'


    tipo_medida_id = fields.Many2one(
        string="Tipo de Medida",
        comodel_name="com.camilasport.tipo.medida",
    )

    medida = fields.Float(string="Medida", )
