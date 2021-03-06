# -*- coding: utf-8 -*-
{
    'name': "University"   ,

    'summary': """
        managment system for university""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application' : True ,

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data':  [
    'security/security_groups.xml',
    'security/ir.model.access.csv',

    'views/views.xml' ,
    'wizard/operation_wizard_view.xml',
    'reports/report_template.xml',
    'reports/report_action.xml',
    'reports/student_report_template.xml',
    'views/employee_inherit.xml',

    'views/faculties_view.xml'
    
   

    ],

    'demo': [
        'demo/demo.xml',
    ],
   
}