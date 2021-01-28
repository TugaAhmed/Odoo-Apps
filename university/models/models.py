
from odoo import models,fields 


class Students(models.Model) :
	_name = 'university.students'


	name = fields.Char(string='Studnet Name')
	age  = fields.Integer(string='Age')

	







