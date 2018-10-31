from setuptools import setup

setup(
    name='bibtexprune',
    version='1.0',
    packages=['bibtexprune'],
    install_requires=['bibtexparser'],
    entry_points={
        'console_scripts': [
            'bibtexprune = bibtexprune:main'
            ]
        }
    )
