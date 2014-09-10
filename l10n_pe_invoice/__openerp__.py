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
    'name': 'RUC and DNI Validation on Invoice',
    'version': '1.1',
    'category': 'Invoice Management',
    'depends': ['base', 'account', 'base_vat', 'l10n_pe_multifunctions'],
    'author': 'Vauxoo',
    'description': """
Validation for invoice when exceeding minimum amount.
=========================================================

This module modifies the invoice workflow in order to validate RUC and DNI
in Invoice that exceeds minimum amount set by configuration wizard.
    """,
    'website': 'http://www.openerp.com',
    'data': [
        'workflow/invoice_workflow.xml',
        'view/invoice_conf_view.xml',
        'view/account_invoice_sup_inv_num_req.xml'
    ],
    'test': [
        'test/limit_amount_inv.yml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
