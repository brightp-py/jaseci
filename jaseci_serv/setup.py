from setuptools import setup, find_packages
setup(
    name='jaseci_serv',
    version='1.2.1',
    packages=find_packages(include=['jaseci_serv', 'jaseci_serv.*']),
    scripts=['manage.py'],
    install_requires=[
        'jaseci',
        'Django>=3.0.3,<3.1.0',
        'djangorestframework>=3.11.0,<3.12.0',
        'django-rest-knox>=4.1.0,<4.2.0',
        'django-rest-passwordreset>=1.1.0,<1.2.0',
        'drf-yasg>=1.20.0,<1.21.0',
        'markdown>=3.2.1,<3.3.0',
        'psycopg2-binary>=2,<3',
        'sphinx>=2.4.3,<2.5.0',
        'sphinx_rtd_theme',
        'django-cors-headers',

    ],
    # package_data={"": ["*.ini"], },
    entry_points={
        'console_scripts': [
            'jsserv = jaseci_serv.manage:main'
        ]
    })
