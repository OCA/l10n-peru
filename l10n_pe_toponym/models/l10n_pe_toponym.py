# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.base.models.res_country import location_name_search


class L10npeCountryProvince(models.Model):
    _name = 'l10n_pe.res.country.province'
    _description = 'Lista de Provincias'

    def _default_country_id(self):
        model_res_country = self.env['res.country']
        return model_res_country.search([('code', '=', 'PE')])

    state_id = fields.Many2one(
        'res.country.state',
        string='Departamento',
        required=True
    )
    country_id = fields.Many2one(
        'res.country',
        default=_default_country_id,
        string='País'
    )
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)

    name_search = location_name_search

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)',
         'Código de la Provincia debe ser único por Departamento!')
    ]


class L10npeCountryDistrict(models.Model):
    _name = 'l10n_pe.res.country.district'
    _description = 'Lista de Distritos'

    def _default_country_id(self):
        model_res_country = self.env['res.country']
        return model_res_country.search([('code', '=', 'PE')])

    province_id = fields.Many2one(
        'l10n_pe.res.country.province',
        string='Provincia',
        required=True
    )
    state_id = fields.Many2one(
        'res.country.state',
        related='province_id.state_id',
        string='Departamento'
    )
    country_id = fields.Many2one(
        'res.country',
        default=_default_country_id,
        string='País'
    )
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)

    name_search = location_name_search

    _sql_constraints = [
        ('name_code_uniq', 'unique(province_id, code)',
         'Código del Distrito debe ser único por Provincia!')
    ]
