# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class Prenda(models.Model):
    _name = 'com.camilasport.prenda'


    vestimenta = fields.Selection(
        string="Vestimenta",
        selection=[
                ('vi', 'Vestimenta inteligente'),
                ('vc', 'Vestimenta Casual'),
                ('vf', 'Vestimenta Formal'),
                ('vs', 'Vestimenta Semiformal'),
                ('e', 'Etiqueta'),
                ('vct', 'Vestimenta Casual'),
                ('vd', 'Vestimenta Deportiva'),
                ('ve', 'Vestimenta Escolar'),
        ],
    )

    tipo_prenda_id = fields.Many2one(
        string="Tipo de Prenda",
        comodel_name="com.camilasport.tipo.prenda",)

    medida_ids = fields.Many2many(
        string="Medidas",
        comodel_name="com.camilasport.medidas",
        relation="prenda_medidas_rel",
        column1="prenda_id",
        column2="medida_id"
    )

    precio = fields.Integer(string="Precio")
