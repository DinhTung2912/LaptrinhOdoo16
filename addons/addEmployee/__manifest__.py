{
    'name': 'Custom Department',
    'version': '1.0',
    'author': 'Dinh Tung',
    'category': 'Human Resources',
    'summary': 'Custom Department Module',
    'description': """This module inherits view and model of Department.""",
    'depends': ['base', 'hr'],
    'data': [
        'views/employee_department_view.xml'

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
