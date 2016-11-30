# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class Persona(models.Model):
    _name = 'com.camilasport.persona'

    p_nombre = fields.Char(string="Primer Nombre", required=True)
    s_nombre = fields.Char(string="Otros Nombres", )
    a_paterno = fields.Char(string="Apellido Paterno", required=True)
    a_materno = fields.Char(string="Apellido Materno",)

    sexo = fields.Selection(
        string="Sexo",
        selection=[
                ('M', 'Masculino'),
                ('F', 'Femenino'),
        ],
    )

    tipo_identificacion = fields.Selection(
        string="Tipo Identificación",
        selection=[
                ('CC', 'Cédula de Ciudadania'),
                ('TI', 'Cedula de Extranjeria'),
                ('TI', 'Tarjeta de Identidad')
        ], default='CC'
    )

    identificacion = fields.Char(string="Identificación", )
    email = fields.Char(string="E-mail", )
    es_cliente = fields.Boolean(string="Es Cliente")
