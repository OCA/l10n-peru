# -*- coding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: Luis Ernesto García Medina (ernesto_gm@vauxoo.com)
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


from openerp.osv import osv
from openerp.tools.translate import _

import re


class account_invoice(osv.Model):

    _inherit = 'account.invoice'

    def _check_reference_field(self, cr, uid, ids, context=None):
        invoices = self.browse(cr, uid, ids)
        for invoice in invoices:
            if invoice.type == 'in_invoice':
                if invoice.supplier_invoice_number:
                    ref_split = invoice.supplier_invoice_number.split('-')
                    if len(ref_split) == 2:
                        ref_left = ref_split[0]
                        ref_right = ref_split[1]
                        if re.match("[a-zA-Z0-9]+$", ref_left) is None or\
                                re.match("[0-9]+$", ref_right) is None:
                            return False
                    else:
                        return False
        return True

    _constraints = [(_check_reference_field,
                     _("Invalid value \nThe correct format is:\n [alphanumeric\
                       value]-[numeric value]"), ['supplier_invoice_number'])]
