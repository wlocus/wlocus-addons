# © 2019 Jhonatan Eduardo, Wlocus
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'WL Payment GerenciaNet',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: GerenciaNet Implementation',
    'version': '1.0',
    'description': """GerenciaNet Payment Acquirer""",
    'author': 'Wlocus',
    'license': 'AGPL-3',
    'website': 'http://www.wlocus.com.br',
    'contributors': [
        'Jhonatan Eduardo <jhonatanepp@gmail.com>'
    ],
    'depends': ['payment'],
    'data': [
        # 'views/payment_views.xml',
        # 'views/payment_paypal_templates.xml',
        # 'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    # 'post_init_hook': 'create_missing_journal_for_acquirers',
}
