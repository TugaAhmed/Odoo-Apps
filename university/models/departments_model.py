from odoo import models,fields , api
from datetime import date
from odoo.exceptions import UserError




class Departments(models.Model) :
	_name = 'university.departments'

	name = fields.Char(string='Name')
	head_of_department = fields.Many2one('res.users',string='Head Of Department')

	student_ids = fields.One2many('university.students','department_id',string='Students')

	count_sudents = fields.Integer(string='Studnet Count' , compute='count_students' )

	facluty_id = fields.Many2one('faculties' , string='Faculty')


	@api.depends('student_ids')
	def count_students(self) :
		self.count_sudents = 0
		for record in self :
			record.count_sudents = 0 

			record.count_sudents = len(record.student_ids)
			print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS len(record.student_ids)",len(record.student_ids))
			



class Faculties(models.Model) :
	_name = 'faculties'

	name = fields.Char(string='Name')
	dean_name = fields.Char(string='Dean Name')
	department_ids = fields.One2many('university.departments' , 'facluty_id' , string='Departments')








