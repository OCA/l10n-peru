# coding: utf-8
##
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
##
#    Coded by: Edgard Pimentel (pimentelrojas@gmail.com)
#              Luis Torres (luis_t@vauxoo.com)
##
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
#
'''
File to inherit res_partnet to get name & address to partner with your RUC
'''
import requests
from openerp.osv import osv
from lxml import html
from openerp.tools.translate import _


class ResPartner(osv.osv):
    '''
    Inherit res.partner to get your name & address from the xml returned by
    SUNAT
    '''
    _inherit = 'res.partner'

    def button_check_vat(self, cr, uid, ids, context=None):
        '''
        Update name & address partner by SUNAT
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param value: RUC set in partner
        @param context: A standard dictionary
        @return : retrun report
        '''
        if context is None:
            context = {}
        res = super(ResPartner, self).button_check_vat(
            cr, uid, ids, context=context)
        for partner in self.browse(cr, uid, ids, context=context):
            if partner.vat:
                vat = partner.vat[3:]
                if len(vat) == 11:
                    link = 'http://www.sunat.gob.pe/w/wapS01Alias?ruc=%s' % vat
                    client = requests.get(link)
                    client = client.text.replace('\r', '').replace(
                        '\n', '').replace('\t', '')
                    root = html.fromstring(client)
                    if root[2].attrib['id'] == 'frstcard':
                        name = root[2][0][0].text_content().split('-')
                        street = root[2][0][9].text_content()
                        if root[2][0][4].text_content().split(
                                '.')[1] == 'ACTIVO':
                            partner.write({'name': name[1][1:-1],
                                           'street': street[9:]})
                        else:
                            raise osv.except_osv(_('Error!'), _(
                                'Inactive RUC'))
                    else:
                        raise osv.except_osv(_('Error!'), _('Invalid RUC'))
                else:
                    raise osv.except_osv(_('Error!'), _('Invalid RUC'))
        return res
