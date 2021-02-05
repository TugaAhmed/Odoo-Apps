
from odoo import models,fields , api
from datetime import date
from odoo.exceptions import UserError



class EmployeeInherit(models.Model):
	_inherit = 'hr.employee'


	degree = fields.Selection(string='Degree' , selection= [('ms','Master') , ('pdf','PHD') , ('postdoc','Post Doc')] )



	def add_pin_code(self) :
		self.pin = "123"