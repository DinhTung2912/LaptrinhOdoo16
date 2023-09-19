{
    'name': 'Library Management',
    'summary': 'Library Management Module',
    'description': 'Module for managing library and student information',
    'version': '1.0',
    'author': 'Dinh Tung',
    'category': 'Uncategorized',
    'depends': ['base'],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        'views/library_management_views.xml',
        'views/my_books_views.xml',

        'views/library_menu.xml',
    ],
    'installable': True,
    'application': True,
}
