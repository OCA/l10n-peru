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
from openerp.osv import osv


class crm_lead2opportunity_partner(osv.osv_memory):
    _inherit = 'crm.lead2opportunity.partner'

    def _create_partner(self, cr, uid, ids, context=None):
        res = super(crm_lead2opportunity_partner, self)._create_partner(
            cr, uid, ids, context=context)
        if res:
            crm_lead_obj = self.pool.get('crm.lead')
            brw_crm = crm_lead_obj.browse(
                cr, uid, [res.keys()[0]], context=context)[0]
            self.pool.get(
                'res.partner').write(
                    cr, uid,
                    res.values()[0], {
                        'l10n_pe_district_id': brw_crm.l10n_pe_district_id and
                        brw_crm.l10n_pe_district_id.id or False,
                        'l10n_pe_province_id': brw_crm.l10n_pe_province_id and
                        brw_crm.l10n_pe_province_id.id or False},
                    context=context)
        return res
