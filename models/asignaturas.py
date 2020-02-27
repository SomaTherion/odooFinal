from odoo import models, fields, api

class Asignaturas(models.Model):
    _name = 'insti.asignaturas'
    cod = fields.Char('cod', required=True)
    nombre = fields.Char('Nombre', required=True)
    instituto = fields.Many2one('insti.institutos', 'Instituto')


    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

