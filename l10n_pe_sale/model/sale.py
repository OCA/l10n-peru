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

from openerp.osv import osv
from openerp.tools.translate import _


class sale_order(osv.Model):

    _inherit = 'sale.order'

    def check_ruc_dni(self, cr, uid, ids, context=None):
        country = False
        vat_pe = False
        for sale_order in self.browse(cr, uid, ids, context=context):
            partner = sale_order.partner_id and \
                sale_order.partner_id.commercial_partner_id or False
            if sale_order.user_id and sale_order.user_id.company_id and \
                    sale_order.user_id.company_id.partner_id and \
                    sale_order.user_id.company_id.partner_id.country_id and \
                    sale_order.user_id.company_id.partner_id.country_id.name:
                country = self.pool.get('account.invoice').unaccented(
                    sale_order.user_id.company_id.
                    partner_id.country_id.name).lower() == 'peru'
            if sale_order.user_id and sale_order.user_id.company_id and \
                    sale_order.user_id.company_id.partner_id and \
                    sale_order.user_id.company_id.partner_id.vat:
                if (sale_order.user_id.company_id.
                        partner_id.vat).lower()[0:2] == 'pe':
                    vat_pe = sale_order.user_id.company_id.partner_id.vat
            if not ((country and vat_pe) or
                    (country and not vat_pe) or
                    (not country and vat_pe)):
                return True
            elif partner.vat:
                return True
        return False

    def check_ruc(self, cr, uid, ids, context=None):
        country = False
        vat_pe = False
        for sale_order in self.browse(cr, uid, ids, context=context):
            partner = sale_order.partner_id and \
                sale_order.partner_id.commercial_partner_id or False
            partner_company = partner.is_company
            if sale_order.user_id and sale_order.user_id.company_id and \
                    sale_order.user_id.company_id.partner_id and \
                    sale_order.user_id.company_id.partner_id.country_id and \
                    sale_order.user_id.company_id.partner_id.country_id.name:
                country = self.pool.get('account.invoice').unaccented(
                    sale_order.user_id.company_id.
                    partner_id.country_id.name).lower() == 'peru'
            if sale_order.user_id and sale_order.user_id.company_id and \
                    sale_order.user_id.company_id.partner_id and \
                    sale_order.user_id.company_id.partner_id.vat:
                if (sale_order.user_id.company_id.
                        partner_id.vat).lower()[0:2] == 'pe':
                    vat_pe = sale_order.user_id.company_id.partner_id.vat
            if not ((country and vat_pe) or
                    (country and not vat_pe) or
                    (not country and vat_pe)):
                return True
            elif (partner_company and partner.vat) or (not partner_company):
                return True
        return False

    def show_message_ruc_dni(self, cr, uid, ids, context=None):
        result = self.check_ruc(cr, uid, ids, context=context)
        if not result:
            raise osv.except_osv(_('Invalid Action!'), _('Not RUC set'))

    def show_message_ruc_dni2(self, cr, uid, ids, context=None):
        result = self.check_ruc_dni(cr, uid, ids, context=context)
        if not result:
            raise osv.except_osv(_('Invalid Action!'), _('Not RUC or DNI set'))
