# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.base.models.res_country import location_name_search


class L10npeCountryProvince(models.Model):
    _name = 'l10n_pe.res.country.province'
    _description = 'Lista de Provincias'

    state_id = fields.Many2one('res.country.state', string='Departamento', required=True)
    country_id = fields.Many2one('res.country', related='state_id.country_id', string=u'País')
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string=u'Código', required=True)

    name_search = location_name_search

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)', u'Código de la Provincia debe ser único por Departamento!')
    ]


class L10npeCountryDistrict(models.Model):
    _name = 'l10n_pe.res.country.district'
    _description = 'Lista de Distritos'

    province_id = fields.Many2one('l10n_pe.res.country.province', string='Provincia', required=True)
    state_id = fields.Many2one('res.country.state', related='province_id.state_id', string='Departamento')
    country_id = fields.Many2one('res.country', related='state_id.country_id', string=u'País')
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string=u'Código', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(province_id, code)', u'Código de la Distrito debe ser único por Provincia!')
    ]
