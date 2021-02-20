from odoo import models, fields
class MyTask(models.Model):
 _inherit = 'my.task'
 priority = fields.Selection([('0','Low'), ('1','Normal'), ('2','High')], 'Priority',default='1')
 kanban_state = fields.Selection([('normal', 'Pedido'),('blocked', 'Haciendose'),('done', 'Servido')],'Kanban State',  default='normal')