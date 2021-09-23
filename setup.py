from setuptools import find_packages
from setuptools import setup

setup(
    name='eq-django-admin-row-actions',
    version='0.0.7',
    description='README.md',
    author='Equality',
    author_email='proyectos@equality.coop',
    packages=find_packages(),
    install_requires=[
        'six',
    ],
    package_data={
        'eq_django_admin_row_actions': [
            'static/css/*.css',
            'static/js/*.js',
            'templates/django_admin_row_actions/*.html',
        ]
    },
    include_package_data=True,
)
