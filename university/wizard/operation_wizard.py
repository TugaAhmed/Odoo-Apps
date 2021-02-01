from odoo import api , fields , models 


class operation_wizard(models.TransientModel) :
	_name = 'operation.wizard'


	student_ids = fields.Many2many('university.students' , string='Students')



	def put_recommendation(self) :
		for student in self.student_ids :
			student.recommendation_letter = student.name + " is a smart student"


	def delete_students(self) :
		self.student_ids.unlink()



class students_report_wizard(models.TransientModel) :
	_name = 'students.report.wizard'

	start_date = fields.Date('Start Date')
	end_date = fields.Date('End Date')



	def print_report(self , data = False):

        
		data = {
            'start_date': self.start_date ,
            'end_date':  self.end_date ,}

        # return self.evn.ref('module_name.report_action_id')
		return self.env.ref('university.student_report_action').report_action(self, data=data)



