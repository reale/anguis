from setuptools import setup

setup(
    name = 'anguis',
    version = '0.2.3',
    description = 'A generic key-store library',
    packages = [ 'anguis' ],
    author = 'Roberto Reale',
    author_email = 'roberto@reale.me',
    url = 'https://github.com/reale/anguis',
    keywords = [ 'cache', 'key-value store' ],
    install_requires = [
        'python-etcd',
    ],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
