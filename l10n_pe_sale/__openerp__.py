# -*- coding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: Julio Serna (julio@vauxoo.com)
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
##############################################################################

{
    'name' : 'RUC and DIN Validation on Sales',
    'version' : '1.1',
    'category': 'Sale Management',
    'depends' : ['base','sale', 'base_vat','l10n_pe_multifunctions'],
    'author' : 'Vauxoo',
    'description': """
Validation for sale when exceeding minimum amount.
=========================================================

This module modifies the sale workflow in order to validate RUC and DIN in sale that
exceeds minimum amount set by configuration wizard.
    """,
    'website': 'http://www.openerp.com',
    'data': [
        'workflow/sale_workflow.xml',
        'view/sale_conf_view.xml'
    ],
    'test': [
        'test/sale_limit_amount_test.yml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
