from odoo import models , api 



class studentReport(models.AbstractModel) :
	_name = 'report.university.student_template_id'


	def _get_report_values(self , docids , data) :

		gender_value = data['gender']


		records = self.env['university.students'].search([ ('gender' , '=' , gender_value) ])

		return {'docs' : records }






