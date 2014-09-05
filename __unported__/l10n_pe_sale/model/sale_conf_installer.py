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


from openerp.osv import fields, osv

class sale_configuration(osv.osv_memory):
    _inherit = 'sale.config.settings'
    
    _columns = {
    'limit_amount': fields.integer('limit to require a validation of ruc or dni',
        help="Amount after which validation of sale is required."),
    }

    _defaults = {
        'limit_amount': 700,
    }

    def get_default_limit_amount(self, cr, uid, fields, context=None):
        ir_model_data = self.pool.get('ir.model.data')
        transition = ir_model_data.get_object(cr, uid, 'l10n_pe_sale', 'trans_draft_wait')
        value = transition.condition.split()
        return {'limit_amount': int(value[2])}

    def set_limit_amount(self, cr, uid, ids, context=None):
        ir_model_data = self.pool.get('ir.model.data')
        config = self.browse(cr, uid, ids[0], context)
        waiting = ir_model_data.get_object(cr, uid, 'l10n_pe_sale', 'trans_draft_wait')
        waiting.write({'condition': 'amount_total >= %s' % config.limit_amount})
        waiting = ir_model_data.get_object(cr, uid, 'l10n_pe_sale', 'trans_wait_router')
        waiting.write({'condition': 'amount_total < %s' % config.limit_amount})
        waiting = ir_model_data.get_object(cr, uid, 'l10n_pe_sale', 'trans_sent_wait')
        waiting.write({'condition': 'amount_total >= %s' % config.limit_amount})
        waiting = ir_model_data.get_object(cr, uid, 'l10n_pe_sale', 'trans_wait_check')
        waiting.write({'condition': 'amount_total >= %s' % config.limit_amount})

