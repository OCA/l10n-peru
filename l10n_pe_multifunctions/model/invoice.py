# -*- coding: utf-8 -*-                                                       #
###############################################################################
#    Module Writen to OpenERP, Open Source Management Solution                #
#                                                                             #
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com                        #
#    All Rights Reserved.                                                     #
#    info@vauxoo.com                                                          #
###############################################################################
#    Coded by: Sabrina Romero (sabrina@vauxoo.com)                            #
###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU Affero General Public License as           #
#    published by the Free Software Foundation, either version 3 of the       #
#    License, or (at your option) any later version.                          #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU Affero General Public License for more details.                      #
#                                                                             #
#    You should have received a copy of the GNU Affero General Public License #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
###############################################################################
"""
This file adds validations that will be used in several modules
of the Peruvian location. In this case unaccented method its added
in account.invoice model for l10n_pe_invoice and l10n_pe_sale.
"""

from openerp.osv import osv

import unicodedata


class account_invoice(osv.Model):

    """
    This class adds methods for validations to account.invoice model.
    """
    _inherit = 'account.invoice'

    def unaccented(self, cadena):
        """
            This method receives a string and returns the same
            string without accents.
        """
        cadena = ''.join((c for c in unicodedata.normalize(
            'NFD',
            unicode(cadena)) if unicodedata.category(c) != 'Mn'))
        return cadena.decode()
