# Copyright 2016-2017 Colossus Peru - Juan D. Salcedo Salazar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
import tempfile
import os

from odoo import api, fields, models, tools

from ..gen_src.gen_data_toponym import gen_ubigeo_data_xml


_logger = logging.getLogger(__name__)


class L10nPeToponymImportWizard(models.TransientModel):
    _name = 'l10n_pe.toponym.import.wizard'
    _inherit = 'res.config.installer'

    import_fail = fields.Boolean(default=False)

    @api.multi
    def import_local(self):
        res = super(L10nPeToponymImportWizard, self).execute()
        path = os.path.join('l10n_pe_toponym', 'wizard', 'ubigeo_data.xml')
        with tools.file_open(path) as fp:
            tools.convert_xml_import(
                self._cr, 'l10n_pe_toponym', fp, {}, 'init', noupdate=True)
        return res

    @api.multi
    def execute(self):
        import requests
        src_file = tempfile.NamedTemporaryFile(delete=False)
        dest_file = tempfile.NamedTemporaryFile('w', delete=False)
        try:
            response = requests.get(
                'http://webinei.inei.gob.pe:8080/sisconcode/web/ubigeo/'
                'listaBusquedaUbigeoPorUbicacionGeograficaXls/5/1/1/null/null/null')
            response.raise_for_status()
            src_file.write(response.content)
            # Generate XML and reopen it
            gen_ubigeo_data_xml(src_file.name, dest_file.name)
            tools.convert_xml_import(
                self._cr, 'l10n_pe_toponym', dest_file.name, {}, 'init', noupdate=True)
        except requests.exceptions.HTTPError:  # pragma: no cover
            _logger.exception('HTTP Error while importing data')
            self.import_fail = True
            return {
                'name': 'Importar Data de Ubigeo Peruano',
                'type': 'ir.actions.act_window',
                'res_model': 'l10n_pe.toponym.import.wizard',
                'view_id': self.env.ref(
                    'l10n_pe_toponym.l10n_pe_toponym_import_wizard').id,
                'view_type': 'form',
                'view_mode': 'form',
                'res_id': self.id,
                'target': 'new',
            }
        finally:
            src_file.close()
            dest_file.close()
            os.remove(src_file.name)
            os.remove(dest_file.name)
