from odoo import models, api, fields

class ProjetctTask(models.Model):
    _inherit = "project.task"

    lavoro_chiuso = fields.Boolean(string='Lavoro chiuso')
    data_chiusura = fields.Date(string='Data chiusura lavoro')
    lavoro_nonfatturabile = fields.Boolean(string='Lavoro non fatturabile')


    
