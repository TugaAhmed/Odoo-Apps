from odoo import fields , models , api 


class StudentReport(models.AbstractModel) :
	# _name = 'report.module_name.report_template_id'
	_name = 'report.university.students_template_id'




	@api.model
	def _get_report_values(self, docids, data):

		if 'start_date' in data  or 'end_date' in data :
			print("############################## data",data)
			start_date = data['start_date']
			end_date = data['end_date']

			result = self.env['university.students'].search([('registration_date','>=',start_date), 
				                                  ('registration_date', '<=' , end_date)]) 

			print("DDDDDDDDDDDDDDDDDDDDDDDDD docids",self)
			return { 'docs' : result} 
		else :
			print("DDDDDDDDDDDDDDDDDDDDDDDDD docids",self)

			result = self.env['university.students'].search([('id','in',docids), 
				                                 ]) 

			return	{ 'docs' : result} 






