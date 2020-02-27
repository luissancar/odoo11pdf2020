from odoo import models, fields, api

class Administracion(models.Model):
    _name = 'empresa.administracion'
    numAdm = fields.Integer('Numero de Administrador', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    salario = fields.Integer('Salario', required=True)

    def name_get(self):
        res = []

        for record in self:
            num = record.numAdm
            res.append((record.id, num))
        return res