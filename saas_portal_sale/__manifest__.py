{
    'name': "Saas Portal Sale",
    'author': "IT-Projects LLC, Ildar Nasyrov, Nicolas JEUDY",
    'license': 'LGPL-3',
    'support': 'apps@it-projects.info',
    'website': 'https://it-projects.info',
    'category': 'SaaS',
    'summary': 'Sells SaaS products in the Webshop',
    'version': '11.0.1.1.0',
    'depends': [
        'sale',
        'website_sale',
        'saas_portal',
        'product_price_factor',
        'contract',
    ],
    'data': [
        'views/product_template_views.xml',
        'views/product_attribute_views.xml',
        'views/saas_portal.xml',
        'data/mail_template_data.xml',
        'data/ir_config_parameter.xml',
    ],
}
