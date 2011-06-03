try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='whatcouch-quickstart-example',
    version='1.0dev3',
    description='',
    author='',
    author_email='',
    url='',
    license='BSD-derived (http://code.google.com/p/whatcouch/wiki/License)',
    install_requires=[
        "Pylons>=1.0",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'whatcouchquickstartexample': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'whatcouchquickstartexample': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = whatcouchquickstartexample.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
