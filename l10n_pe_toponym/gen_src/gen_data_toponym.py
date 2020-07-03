# Copyright 2016-2017 Colossus Peru - Juan D. Salcedo Salazar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import codecs
import logging
import os
from datetime import datetime

try:
    import xlrd
except ImportError:
    xlrd = None

_logger = logging.getLogger(__name__)

DEPA_KEY = 'DEPARTAMENTO'
PROV_KEY = 'PROVINCIA'
DIST_KEY = 'DISTRITO'


class XlsDictReader:
    """
    Esta clase fue inspirada en la clase XlsDictReader de la localización Española
    disponible en: 'https://github.com/OCA/l10n-spain/blob/12.0/
    l10n_es_partner/gen_src/gen_data_banks.py'
    An XLS reader which will iterate over lines in the given file, taking
    first column as the keys for the data dictionary.
    """
    def __init__(self, path, sheet_number=0):
        if not xlrd:  # pragma: no cover
            raise Exception("Librería xlrd no encontrada.")
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_index(sheet_number)
        self.col_values = (1, 4, 5)
        self.header = [self.sheet.cell_value(1, ncol) for ncol in self.col_values]
        self.nrow = 2

    def __next__(self):
        if self.nrow >= self.sheet.nrows:
            self.nrow = 2
            raise StopIteration
        vals = []
        for ncol in self.col_values:
            val = self.sheet.cell_value(self.nrow, ncol)
            cell_type = self.sheet.cell_type(self.nrow, ncol)
            if cell_type == xlrd.XL_CELL_DATE:  # pragma: no cover
                vals.append(datetime(
                    *xlrd.xldate_as_tuple(val, self.workbook.datemode)))
            elif cell_type == xlrd.XL_CELL_BOOLEAN:  # pragma: no cover
                vals.append(bool(val))
            else:
                vals.append(val)
        self.nrow += 1
        return dict((self.header[x], vals[x]) for x in range(0, len(self.header)))

    def __iter__(self):
        self.nrow = 2
        return self


def gen_ubigeo_data_xml(src_path, dest_path):
    indent = "    "
    # Abrir el archivo que contine la información del ubigeo peruano
    try:
        reader = XlsDictReader(src_path)
    except IOError:  # pragma: no cover
        _logger.error("File '{}' not found.".format(src_path))
        return

    def valid(fila, key):
        return fila[key] not in ('', ' ') and fila[key] != key

    depas = []
    provs = []
    dists = []

    # Preparar el archivo resultante
    output = codecs.open(dest_path, mode='w', encoding='utf-8')
    output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    output.write('<odoo>\n')
    output.write(indent + '<!-- Departamentos -->\n')
    for row in reader:
        if valid(row, DEPA_KEY):
            code, name = row[DEPA_KEY].split(' ', 1)
            if code not in depas:
                depas.append(code)
                output.write(
                    indent +
                    '<record id="res_country_state_{}" model="res.country.state">'
                    '<field name="name">{}</field><field name="code">{}</field>'
                    '<field name="country_id" ref="base.pe"/></record>\n'
                    .format(code, name, code)
                )
    output.write(indent + '<!-- Provincias -->\n')
    for row in reader:
        if valid(row, PROV_KEY):
            codes = row[DEPA_KEY].split(' ', 1)[0]
            code, name = row[PROV_KEY].split(' ', 1)
            final_code = codes + code
            if final_code not in provs:
                provs.append(final_code)
                output.write(
                    indent +
                    '<record id="l10n_pe_res_country_province_{}" '
                    'model="l10n_pe.res.country.province">'
                    '<field name="name">{}</field><field name="code">{}</field>'
                    '<field name="state_id" ref="res_country_state_{}"/></record>\n'
                    .format(final_code, name, final_code, codes)
                )
    output.write(indent + '<!-- Distritos -->\n')
    for row in reader:
        if valid(row, DIST_KEY):
            codep = row[DEPA_KEY].split(' ', 1)[0] + row[PROV_KEY].split(' ', 1)[0]
            code, name = row[DIST_KEY].split(' ', 1)
            final_code = codep + code
            if final_code not in dists:
                dists.append(final_code)
                output.write(
                    indent +
                    '<record id="l10n_pe_res_country_district_{}" '
                    'model="l10n_pe.res.country.district">'
                    '<field name="name">{}</field><field name="code">{}</field>'
                    '<field name="province_id" ref="l10n_pe_res_country_province_{}"/>'
                    '</record>\n'.format(final_code, name, final_code, codep)
                )
    output.write('</odoo>\n')
    output.close()
    _logger.info('ubigeo_data.xml succesfully generated.')


if __name__ == '__main__':  # pragma: no cover
    dir_path = os.path.os.path.dirname(__file__)
    parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    gen_ubigeo_data_xml(
        'rptUbigeo.xls', os.path.join(parent_path, 'wizard', 'ubigeo_data.xml'))
