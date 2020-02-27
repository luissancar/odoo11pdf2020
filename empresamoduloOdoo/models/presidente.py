from odoo import models, fields, api

class Presidente(models.Model):
    _name = 'empresa.presidente'
    numPresidente = fields.Integer('Numero de presidente', required = True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    fechaEntrada = fields.Date('FechaEntrada', required=True)
    salario = fields.Integer('Salario bonus Presidente', required=True)
