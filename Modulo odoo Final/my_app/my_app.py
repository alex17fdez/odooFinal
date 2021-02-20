# -*- coding: utf-8 -*- 
from odoo import models, fields 
class MyTask(models.Model): 
    _name = 'my.task' 
    _description = 'My Task'
    name = fields.Char('Description', required=False) 

    idPedido = fields.Char('id_pedido', required=False) 
    #nombreEmpleado = fields.Char('Nombre Empleado', required=False) 
    nombreEmpleado = fields.Many2one('res.users', 'Nombre Empleado')
    numeroMesa = fields.Char('Nº Mesa', required=False) 
    bebida = fields.Selection(selection =([('cocacola','Coca Cola'),('nestea','Nestea'),('fanta','Fanta'),('aquarius','Aquarius'),('cerveza','Cerveza'),('vino','Vino'),('agua','Agua')]), string='Bebida',required=False, help='Seleccione Bebida') 
    plato = fields.Many2one('lunch.product', 'Plato', required=False)
    # plato = fields.Char('Plato', required=False) 
    precio = fields.Float('Precio(€)', required=False) 
    dia = fields.Date('Dia del pedido', required=False) 
    hora = fields.Float(string='Hora', required=False)
    tipo_turno = fields.Selection(selection =([('mañana','Mañana'),('tarde','Tarde'),('noche','Noche')]), string='Turno',required=False, help='Seleccione un Turno') 

    is_done = fields.Boolean('Done?') 
    active = fields.Boolean('Active?', default=True)

    def do_marcar(self):
        self.is_done = not self.is_done
        return True
    def do_limpiar(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
