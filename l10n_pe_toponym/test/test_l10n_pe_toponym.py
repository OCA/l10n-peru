# Copyright 2016-2017 Colossus Peru - Juan D. Salcedo Salazar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestL10nPeToponym(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestL10nPeToponym, cls).setUpClass()
        cls.country_peru = cls.env.ref('base.pe')
        cls.wizard = cls.env['l10n_pe.toponym.import.wizard'].create({})

    def test_import_toponyms(self):
        # Se importa el Ubigeo
        self.wizard.import_local()
        state = self.env['res.country.state'].search(
            [('country_id', '=', self.country_peru.id), ('code', '=', '20')]
        )
        self.assertTrue(state)
        provincia = self.env['l10n_pe.res.country.province'].search(
            [('code', '=', '1703')]
        )
        self.assertTrue(provincia)
        distrito = self.env['l10n_pe.res.country.district'].search(
            [('code', '=', '220704')]
        )
        self.assertTrue(distrito)
        # Nos aseguramos que los registros no existen
        state.unlink()
        provincia.unlink()
        distrito.unlink()
        # Se importa el Ubigeo pero ahora desde Internet
        self.wizard.execute()
        state = self.env['res.country.state'].search(
            [('country_id', '=', self.country_peru.id), ('code', '=', '20')]
        )
        self.assertTrue(state)
        provincia = self.env['l10n_pe.res.country.province'].search(
            [('code', '=', '1703')]
        )
        self.assertTrue(provincia)
        distrito = self.env['l10n_pe.res.country.district'].search(
            [('code', '=', '220704')]
        )
        self.assertTrue(distrito)
