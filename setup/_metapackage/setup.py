import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-l10n-peru",
    description="Meta package for oca-l10n-peru Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-l10n_pe_add_series_field',
        'odoo8-addon-l10n_pe_base_vat_split',
        'odoo8-addon-l10n_pe_crm_lead',
        'odoo8-addon-l10n_pe_invoice',
        'odoo8-addon-l10n_pe_multifunctions',
        'odoo8-addon-l10n_pe_toponyms',
        'odoo8-addon-l10n_pe_vat_sunat_validation',
        'odoo8-addon-opl',
        'odoo8-addon-opl_all',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
