# -*- coding: utf-8 -*-                                                       #
##
#    Module Writen to OpenERP, Open Source Management Solution                #
#                                                                             #
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com                        #
#    All Rights Reserved.                                                     #
#    info@vauxoo.com                                                          #
##
#    Coded by: Sabrina Romero (sabrina@vauxoo.com)                            #
##
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
##

{"name": "OpenERP Peruvian Localization",
    "version": "",
    "author": "Vauxoo",
    "category": "Localization/Application",
    "description": """
Install all apps needed to comply with Peruvian laws
====================================================
This module will install for you:

From git@github.com:Vauxoo/odoo-peru.git
    l10n_pe_add_series_field
    l10n_pe_base_vat_split
    l10n_pe_crm_lead
    l10n_pe_invoice
    l10n_pe_sale
    l10n_pe_toponyms
    """,
    "website": "http://www.vauxoo.com",
    "license": "AGPL-3",
    "depends": [
#               "l10n_pe_add_series_field",
#               "l10n_pe_base_vat_split",
#               "l10n_pe_crm_lead",
#               "l10n_pe_invoice",
#               "l10n_pe_multifunctions",
#               "l10n_pe_sale",
                "l10n_pe_toponyms",
# End list of all oficial modules.
    ],
    "demo": [],
    "data": [],
    'test': [],
    "installable": True,
    "active": False, }
