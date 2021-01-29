
from odoo import models,fields 


class Students(models.Model) :
	_name = 'university.students'


	name = fields.Char(string='Studnet Name')
	age  = fields.Integer(string='Age')
	note = fields.Text(string='Note')
	weight = fields.Float(string='Weight')
	is_foreigner = fields.Boolean(string='Is Foreigner')
	birth_date = fields.Date(string='Birth Date')
	registration_date = fields.Datetime(string='Registration Date')
	gender = fields.Selection(string='Gender' , selection= [ ('male' , 'Male') , ('female','Female')   ] )
	image = fields.Binary(string='Photo')
	recommendation_letter = fields.Html(string='Recommendation Letter ')

	department_id = fields.Many2one('university.departments',string='Department')

	hobby_ids = fields.Many2many('university.hobbies',string='Hobbies')

	vehicle = fields.Reference( [ ('car','Car') , ('train','Train') , ('bus','Bus') ]  )

	head_of_department = fields.Char(string='Head of Department' , related='department_id.head_of_department')



class Departments(models.Model) :
	_name = 'university.departments'

	name = fields.Char(string='Name')
	head_of_department = fields.Char(string='Head Of Department')

	student_ids = fields.One2many('university.students','department_id',string='Students')


class hobbies(models.Model) :
	_name = 'university.hobbies'

	name = fields.Char(string='Hobby Name')
	hobby_type = fields.Selection(string='Type' , selection= [('sport','Sport') , ('music','Music') , ('art' , 'Art') , ('other','Other') ]  )




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




	







