from openerp.tests import common
import os
import openerp.tools as tools
from openerp import modules
import logging
_logger = logging.getLogger(__name__)


class ReTest(common.TransactionCase):

    """Test againt modules like account, sale, purchase
    """

    def setUp(self):
        super(ReTest, self).setUp()
        self.test_deprecate = [
            # Dont use this test because procurement module changed the
            # make_to_order of product
            'test/picking_order_policy.yml',
            # Dont use this test because product is used like service and try
            # to create picking
            'test/manual_order_policy.yml',
            # Dont use because purchase_double_validation modified flow of
            # purchase module
            'test/process/cancel_order.yml',
            # Dont use because purchase_double_validation modified flow of
            # purchase module
            'test/process/rfq2order2done.yml',

        ]

    def test_reload_test(self):
        if tools.config.options['test_enable']:
            cr, uid = self.cr, self.uid
            module_info = modules.load_information_from_description_file(
                "l10n_pe_retest")
            for dat in module_info.get('depends', []):
                cr.commit()
                try:
                    mod_info = modules.load_information_from_description_file(
                        dat)
                    for test_module in mod_info.get('test', []):
                        if test_module in self.test_deprecate:
                            continue
                        pathname = os.path.join(dat, test_module)
                        fp = tools.file_open(pathname)
                        _logger.info(
                            "Try againt Test: {} of Module: {}".format(
                                test_module, dat))
                        try:
                            tools.convert_yaml_import(
                                cr, dat, fp, kind="test", idref={},
                                mode="init")
                        except Exception:
                            _logger.exception(
                                'module %s: an exception occurred in a test',
                                dat)
                finally:
                    if tools.config.options['test_commit']:
                        cr.commit()
                    else:
                        cr.rollback()
