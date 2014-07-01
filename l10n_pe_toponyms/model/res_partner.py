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
from openerp.osv import osv, fields
from openerp import SUPERUSER_ID
from openerp.tools.translate import _
from lxml import etree

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
        'l10n_pe_province_id': fields.many2one("res.country.province", 'Province',
            domain="[('state_id','=',state_id)]"),
        'l10n_pe_district_id': fields.many2one("res.country.district", 'District',
            domain="[('province_id','=',l10n_pe_province_id)]"),
    }
    
    def _get_default_country_id(self, cr, uid, context=None):
        country_obj = self.pool.get('res.country')
        ids = country_obj.search(cr, uid, [('code', '=', 'PE'), ], limit=1)
        id = ids and ids[0] or False
        return id

    def fields_view_get_address(self, cr, uid, arch, context=None):
        if context is None:
            context = {}
        street = _('Street...')
        street2 = _('Colony...')
        province = _('Province...')
        district = _('District...')
        cp = _('ZIP')
        state = _('State')
        country = _('Country...')
        city2 = _('City...')
        res = super(res_partner, self).fields_view_get_address(cr, uid, arch, context=context)
        user_obj = self.pool.get('res.users')
        fmt = user_obj.browse(cr, SUPERUSER_ID, uid, context).company_id.country_id
        fmt = fmt and fmt.address_format
        city = '<field name="city" placeholder="City" style="width: 40%%"/>'
        for name, field in self._columns.items():
            if name == 'city_id':
                city = '<field name="city" modifiers="{&quot;invisible&quot;: true}" placeholder="%s" style="width: 50%%" invisible="1"/><field name="city_id" on_change="onchange_city(city_id)" placeholder="%s" style="width: 40%%"/>' % (city2, city2)
        layouts = {
            'PE%(street)s\n%(street2)s %(city)s\n%(state_name)s %(country_name)s %(zip)s': """
                    <group>
                        <group>
                            <label for="type" attrs="{'invisible': [('parent_id','=', False)]}"/>
                            <div attrs="{'invisible': [('parent_id','=', False)]}" name="div_type">
                                <field class="oe_inline"
                                    name="type"/>
                                <label for="use_parent_address" class="oe_edit_only"/>
                                <field name="use_parent_address" class="oe_edit_only oe_inline"
                                    on_change="onchange_address(use_parent_address, parent_id)"/>
                            </div>

                            <label for="street" string="Address"/>
                            <div>
                                <field name="street" placeholder="%s"/>
                                <field name="street2" placeholder="%s"/>
                                <div class="address_format">
                                    %s
                                    <field name="state_id" class="oe_no_button" placeholder="%s" style="width: 37%%" options='{"no_open": True}' on_change="onchange_state(state_id)"/>
                                    <field name="zip" placeholder="%s" style="width: 20%%"/>
                                </div>
                                <field name="l10n_pe_province_id" placeholder="%s" class="oe_no_button" style="width: 48%%" options='{"no_open": True}'/>
                                <field name="l10n_pe_district_id" placeholder="%s" class="oe_no_button" style="width: 48%%" options='{"no_open": True}'/>
                                <field name="country_id" placeholder="%s" class="oe_no_button" options='{"no_open": True}'/>
                            </div>
                            <field name="website" widget="url" placeholder="e.g. www.openerp.com"/>
                        </group>
                        <group>
                            <field name="function" placeholder="e.g. Sales Director"
                                attrs="{'invisible': [('is_company','=', True)]}"/>
                            <field name="phone" placeholder="e.g. +32.81.81.37.00"/>
                            <field name="mobile"/>
                            <field name="fax"/>
                            <field name="email" widget="email"/>
                            <field name="title" domain="[('domain', '=', 'contact')]"
                                options='{"no_open": True}' attrs="{'invisible': [('is_company','=', True)]}" />
                        </group>
                    </group>
            """ % (street, street2, city, state, cp, province, district, country)
        }
        for k, v in layouts.items():
            if fmt and (k in fmt):
                doc = etree.fromstring(res)
                for node in doc.xpath("//form/sheet/group"):
                    tree = etree.fromstring(v)
                    node.getparent().replace(node, tree)
                arch = etree.tostring(doc)
            else:
                arch = res
        return arch

    def fields_view_get(self, cr, user, view_id=None, view_type='form',
        context=None, toolbar=False, submenu=False):
        if (not view_id) and (view_type == 'form') and context and context.get(
            'force_email', False):
            view_id = self.pool.get('ir.model.data').get_object_reference(
                cr, user, 'base', 'view_partner_simple_form')[1]
        res = super(res_partner, self).fields_view_get(
            cr, user, view_id, view_type, context, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            fields_get = self.fields_get(cr, user, [
                'l10n_pe_province_id', 'l10n_pe_district_id'], context)
            res['fields'].update(fields_get)
        return res
        
    _defaults = {
        'country_id': _get_default_country_id,
    }

class res_country_province(osv.osv):
    _name = 'res.country.province'
    
    _columns = {
            'name': fields.char('Name', size=64, required=True, select=True),
            'code': fields.char('Code', size=6, required=True, select=True),
            'district_ids': fields.one2many('res.country.district', 'province_id', 'Districts'),
            'state_id': fields.many2one('res.country.state', 'State', select=True, required=True),
        }
        
    _sql_constraints = [
            ('code_uniq', 'unique(code)', _('The code of the province must be unique !'))
        ]
        
class res_country_district(osv.osv):
    _name = 'res.country.district'

    _columns = {
            'name': fields.char('Name', size=64, required=True, select=True),
            'code': fields.char('Code', size=8, required=True, select=True),
            'province_id': fields.many2one('res.country.province', 'Province', required=True, select=True),
        }
        
    _sql_constraints = [
            ('code_uniq', 'unique(code)', _('The code of the district must be unique !'))
        ]
