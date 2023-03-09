{
    'name': 'Top Customers',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['base', 'sale', 'website'],

    'data':  ['views/customers_top.xml',
              'views/qweb_customers.xml',
              ],

    'assets': {
        'web.assets_frontend': [
            'top_customers/static/src/xml/customer.xml',
            'top_customers/static/src/js/customer.js',
            'top_customers/static/src/css/icon.scss',
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,

}
