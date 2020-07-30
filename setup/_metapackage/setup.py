import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-l10n-peru",
    description="Meta package for oca-l10n-peru Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-l10n_pe_toponym',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
