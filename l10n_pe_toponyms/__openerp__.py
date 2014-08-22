# -*- coding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: Luis Torres (luis_t@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name' : 'l10n_pe Geopolitical Distribution',
    'version' : '1.0',
    'category': 'Localization\Peru',
    'depends' : ['base'],
    'author' : 'Vauxoo',
    'description': """
    This module add the fields that require the address of partner in the l10n_pe
    """,
    "website" : "http://www.vauxoo.com/",
    'data': [
        'security/l10n_pe_security.xml',
        'data/res_country_data.xml',
        'view/res_country_view.xml',
        'view/res_company_view.xml',
        'view/country_data.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
