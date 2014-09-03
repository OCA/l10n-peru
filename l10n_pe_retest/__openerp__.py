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
    'name' : 'Re-test',
    'version' : '1.1',
    'category': 'Test',
    'depends' : [
        'warning',
        'l10n_pe_invoice',
        'l10n_pe_sale',
        'account',
        'sale_stock',
        'sale',
        'purchase',
        ],
    'author' : 'Vauxoo',
    'description': """
Before of install modules l10n_pe_invoice and l10n_pe_sale, this module test
============================================================================

    * Test of sale module
    * Test of sale_stock module
    * Test of account module
    * Test of purchase module
    """,
    'website': 'http://www.openerp.com',
    'data': [],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
