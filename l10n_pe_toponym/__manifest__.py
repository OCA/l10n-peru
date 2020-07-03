# Copyright 2019 Salcedo Salazar Juan Diego <juan.salcedo@colossusperu.com>
# Copyright 2019 Lastra Bazán Maicol Demetrio <maicoldemetrio@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Topónimos Peruanos',
    'version': '12.0.1.0.0',
    'author': 'Colossus Peru, '
              'maicoldlb, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/l10n-peru',
    'category': 'Localization',
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': ['requests'],
    },
    'depends': [
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/l10n_pe_toponym_views.xml',
        'wizard/l10n_pe_toponym_wizard.xml',
    ],
    'installable': True,
}
