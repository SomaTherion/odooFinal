from odoo import models, fields, api

class Alumnos(models.Model):
    _name = 'insti.alumnos'
    dni = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    provincia = fields.Many2one('insti.asignaturas', 'Asignatura')
    nota = fields.Float('Nota 1', required=True)
    notaDos = fields.Float('Nota 2', required=True)
    notaTres = fields.Float('Nota 3', required=True)
    notaMedia = fields.Float('Nota Media', compute='calculoMedia')



    @api.one
    def limpiar(self):
        self.nombre = ""
        self.apellidos = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('dni', '=', '0')])
        done_recs.write({'dni': '1'})
        return True

    @api.one
    @api.depends('nota','notaDos','notaTres')
    def calculoMedia(self):
        notaTotal = (self.nota + self.notaDos+self.notaTres)
        self.notaMedia = (notaTotal / 3)
