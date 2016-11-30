# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class Pedido(models.Model):
    _name = 'com.camilasport.pedido'

    fecha_solicitud = fields.Date(string="Fecha Solicitud", default=fields.Date.today())
    fecha_entrega = fields.Date(string="Fecha Entrega", )

    cliente_id = fields.Many2one(
        string="Cliente",
        comodel_name="com.camilasport.persona",
        domain="[('es_cliente', '=', True)]")

    prenda_ids = fields.Many2many(
        string="Prendas",
        comodel_name="com.camilasport.prenda",
        relation="predio_prenda_rel",
        column1="pedido_id",
        column2="prenda_id",
    )

    valor_total = fields.Integer(string="A Cancelar", )
    valor_cancelado = fields.Integer(string="Valor Cancelado", )
    valor_debe = fields.Integer(string="Por Cancelar", )
