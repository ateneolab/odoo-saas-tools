{
    'name': 'SaaS Portal Portal',
    'version': '12.0.1.1.2',
    'author': "IT-Projects LLC, Ildar Nasyrov, Nicolas JEUDY, Coobytec",
    'license': 'LGPL-3',
    'summary': 'Allows your customers to see their SaaS services from the portal',
    'category': 'SaaS',
    "support": "apps@it-projects.info",
    'website': 'https://it-projects.info',
    'depends': ['portal',
                'saas_portal_sale'],
    'data': [
        'views/website_instance_templates.xml',
    ],
    'installable': True,
}
