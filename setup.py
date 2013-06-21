from setuptools import setup

setup(
        name='django-packages-search',
        version='0.1',
 	author='Vahid Rafiei',
        author_email='vahid.rafiei@gmail.com',
        description='A command line tool for searching within djangopackages.com',
	url='https://github.com/vahidR/django-packages-search',
        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
	    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
	    'Topic :: Software Development :: Libraries :: Python Modules',

        ],
        install_requires=['argparse','simplejson','requests'],
        keywords='django, django packages, python',
        py_modules=['dps'],
    )
