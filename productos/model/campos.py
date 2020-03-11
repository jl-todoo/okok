from odoo import fields, models, api

class ModificacionInventario(models.Model):

	_inherit = 'product.template'

	moneda = fields.Float(string = 'Moneda') 
	referencia = fields.Char(string ='Referencia del cliente')
	version = fields.Char(string = 'Version')
	fecha_version = fields.Date(string = 'Fecha version')
	clase_impres = fields.Char(string = 'Clase de Impresion')
	presentacion = fields.Char(string = 'Presentacion')
	tipo_selle = fields.Char(string = 'Tipo de sellado')