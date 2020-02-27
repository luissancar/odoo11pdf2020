# -*- coding: utf-8 -*-
{
    'name': 'Información hospitalaria',
    'version': '1.0',
    'category': 'Finanzas',
    'description': 'Modulo de gestión de hospital',
    'website': 'http://www.iesayala.com',
    'depends': ['base'],
    'data': [
        'views/hospital_view.xml',
        'views/especialidades_view.xml',
        'views/consultas_view.xml',
        'views/medicos_view.xml',
        'views/nacionalidades_view.xml',
        'views/paises_view.xml',
        'views/report.xml'
    ],
    'application': True,
    'installable': True,
}