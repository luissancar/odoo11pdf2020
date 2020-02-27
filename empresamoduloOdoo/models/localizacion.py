from odoo import models, fields, api

class Localizacion(models.Model):
    _name = 'empresa.localizacion'
    pais = fields.Char('Nombre pais', required = True)
    comunidadAutonoma = fields.Char('Nombre comunidad autonoma', required = True)
    municipio = fields.Char('Nombre municipio', required = True)
    postal = fields.Integer('Apartado postal', required = True)
    calle = fields.Char('Nombre calle y numero', required = True)



