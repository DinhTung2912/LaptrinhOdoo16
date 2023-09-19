{
    'name': 'Custom Project Management',
    'version': '1.0',
    'author': 'Dinh Tung',
    'summary': 'Du an quan ly',
    'description': 'Module for managing custom project tasks',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'view/views.xml',
        'view/stage.xml'
    ],
    'application': True,
}
