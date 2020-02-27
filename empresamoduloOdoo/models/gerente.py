from odoo import models, fields, api


class Gerente(models.Model):
    _name = 'empresa.gerente'
    numGer = fields.Integer('Numero de gerente', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    salario = fields.Integer('Salario', required=True)
    numDep = fields.Many2one('empresa.departamento', 'Numero Departamento')

    def name_get(self):
        res = []

        for record in self:
            num = record.numGer
            res.append((record.id, num))
        return res