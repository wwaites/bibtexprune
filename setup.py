from setuptools import setup

setup(
    name='bibtexprune',
    version='1.0',
    description="""\
Prune a large Bibtex database. extract only those entries necessary for
a particular document from the .aux file""",
    author='William Waites',
    url='https://github.com/wwaites/bibtexprune',
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: LaTeX'
    ],
    packages=['bibtexprune'],
    install_requires=['bibtexparser'],
    entry_points={
        'console_scripts': [
            'bibtexprune = bibtexprune:main'
            ]
        }
    )
