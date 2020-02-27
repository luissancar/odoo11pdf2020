from odoo import models, fields, api

class Departamento(models.Model):
    _name = 'empresa.departamento'
    numDep = fields.Integer('Numero Departamento', required=True)
    funcion = fields.Char('Funcion', required=True)
    planta = fields.Char('Planta', required=True)
    piso = fields.Char('Piso', required=True)
    numAdm = fields.Many2one('empresa.administracion', 'Numero Administrador')

    def name_get(self):
        res = []

        for record in self:
            num = record.numDep
            res.append((record.id, num))
        return res