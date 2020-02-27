from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'empresa.empleado'
    numEmpleado = fields.Integer('Numero de empleado', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    edad = fields.Integer('Edad', required = True)
    fechaEntrada = fields.Date('FechaEntrada', required = True)
    salario = fields.Integer('Salario', required=True)
    numGer = fields.Many2one('empresa.gerente', 'Numero Gerente')

