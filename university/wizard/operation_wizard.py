from odoo import fields , models 


class operationWizard(models.TransientModel) :
	_name = 'operation.wizard'

	students_ids = fields.Many2many('university.students' , string='Students')


	def put_recommendation(self) :
		  for record in self.students_ids :
		  	record.recommendation_letter = record.name + " is a smart student"


	def delete_students(self) :
		self.students_ids.unlink()


class student_report_wizard(models.TransientModel) :
	_name = 'student.report.wizard'


	gender = fields.Selection(string='Gender' , selection= [ ('male' , 'Male') , ('female','Female')   ] )




	def print_report(self , data = False) :

		data = { 'gender' : self.gender }  

		return self.env.ref('university.students_report_action').report_action(self,data=data)