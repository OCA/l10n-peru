# Copyright 2019 Salcedo Salazar Juan Diego <juan.salcedo@colossusperu.com>
# Copyright 2019 Lastra Bazán Maicol Demetrio <maicoldemetrio@gmail.com>
# Copyright 2019 Mel Harrison Almerco Poma <melharrison01@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Topónimos Peruanos',
    'version': '13.0.1.0.0',
    'author': 'Colossus Peru E.I.R.L, '
              'maicoldlb, '
              'harri, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/l10n-peru',
    'category': 'Localization',
    'license': 'AGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/l10n_pe_res_country_province_data.xml',
        'data/l10n_pe_res_country_district_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
