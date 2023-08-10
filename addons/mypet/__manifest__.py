{
    'name': "My pet - minhng.info",
    'summary': """My pet models""",
    'description': """Managing pet information""",
    'author': "minhng.info",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.models.access.csv',

    ],
    'data': [

        'views/my_pet_views.xml',
    ],

    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
