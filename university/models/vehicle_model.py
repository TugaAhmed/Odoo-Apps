from odoo import models,fields , api
from datetime import date
from odoo.exceptions import UserError





class bus(models.Model) :
	_name = 'bus'

	name = fields.Char(string='Bus Name')
	color = fields.Char(strint='Color')
	number = fields.Char(string='Number')



class car(models.Model) :
	_name = 'car'

	name = fields.Char(string='car Name')
	color = fields.Char(strint='Color')
	number = fields.Char(string='Number')


class train(models.Model) :
	_name = 'train'

	name = fields.Char(string='Train Name')
	color = fields.Char(strint='Color')
	number = fields.Char(string='Number')




	







