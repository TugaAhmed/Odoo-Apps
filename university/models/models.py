
from odoo import models,fields , api
from datetime import date
from odoo.exceptions import UserError


class StudentRegister(models.Model) :
	_name = 'student.register'

	name = fields.Char(string='Studnet Name')

	first_name = fields.Char(string='First Name')
	second_name = fields.Char(string='Second Name')
	birth_date = fields.Date(string='Birth Date')
	pass_port = fields.Binary(string='Pass port')
	certificate = fields.Binary(string='Certificate')
	studetn_id = fields.Many2one('university.students' , string='Student Id')


	def accept_student(self):

		vals = {'name' : self.name  ,  'first_name' : self.first_name   , 'second_name' : self.second_name}  

		new_student = self.env['university.students'].create(vals)


	def delete_student(self) :
		
		result = self.env['university.students'].search( [('id' , '=', self.student_id )] )

		print("#################################### result",result)	
		result.unlink()





class Students(models.Model) :
	_name = 'university.students'


	name = fields.Char(string='Studnet Name')

	first_name = fields.Char(string='First Name')
	second_name = fields.Char(string='Second Name')


	age  = fields.Integer(string='Age' , compute='compute_age')
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

	phone = fields.Char(string='Phone')

	first_lang = fields.Selection(string='First Language', selection = [ ('ar','Arabic') , ('en','English')  , ('fr','French')  , ('other','Other')   ]    )

	active = fields.Boolean('Active' , default='True')

	state = fields.Selection(string='state' , selection = [('first_year','First Year') , ('second_year','Second Year') , ('third_year','Third Year') , ('graduated','Graduated') ]  , default='first_year')


	def first_to_second(self):
		# self.state = 'second_year'

		vals = {'state' : 'second_year'}

		self.write(vals)

	def second_to_third(self):
		self.state = 'third_year'

	def third_to_graduated(self) :
		self.state = 'graduated'
	
	def graduated_to_third(self) :
		self.state = 'third_year'		


	def put_recommendation(self) :
		self.recommendation_letter = "This Student /" + self.name + "/ is a good student "

	def unlink(self) :

		for record in self :
			if record.registration_date :
				raise UserError("You can no delete registered student ")

		deleted = super(Students , self).unlink()

		return deleted


	def write(self,vals) :

		updated = super(Students , self).write(vals)

		for record in self :
			if record.registration_date :
				
				if record.registration_date.year != 2021 :
					raise UserError("Registration Year must be 2021")

		
		return updated






	@api.model
	def create(self , vals) :

		if vals['first_name'] == False :
			raise UserError("Create Can Not be completed unless you enter first name")

		if vals['second_name'] == False :
			raise UserError("Create Can Not be completed unless you enter second name")	

		new_record = super(Students , self).create(vals)

		new_record.name = new_record.first_name + "  " + new_record.second_name

		return new_record



	@api.onchange('first_lang')
	def onchange_first_lang(self):
		if self.first_lang :
			if self.first_lang == 'ar' :
				self.is_foreigner = False
			else :
				self.is_foreigner = True 		






	@api.constrains('phone')
	def check_phone(self) :
		if self.phone :
			if len(self.phone) != 10 :
				raise UserError("Phone digits must be 10 ")


	@api.depends('birth_date')
	def compute_age(self) : 
		for record in self :
			record.age = 0
			today = date.today()

			if record.birth_date :
				record.age = today.year  - record.birth_date.year





class Departments(models.Model) :
	_name = 'university.departments'

	name = fields.Char(string='Name')
	head_of_department = fields.Char(string='Head Of Department')

	student_ids = fields.One2many('university.students','department_id',string='Students')

	count_sudents = fields.Integer(string='Studnet Count' , compute='count_students' )


	@api.depends('student_ids')
	def count_students(self) :
		self.count_students = 0
		for record in self :
			record.count_sudents = 0 
			record.count_sudents = len(record.student_ids)
			print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS len(record.student_ids)",len(record.student_ids))
			





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




	







