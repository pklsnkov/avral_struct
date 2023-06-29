import os

from setuptools import setup

requires = [
    'avral',
    'pandas',
    'requests',
    'openpyxl'
]

setup(
    name='avral_struct',
    version='0.0.1',
    description='Extension for NextGIS Distributed Geo Task',
    # long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='nextgis',
    author_email='info@nextgis.com',
    url='http://nextgis.com',
    keywords='',
    #packages=['avral_dezhurcad'],
    packages=['avral_struct'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'avral_operations': [
            'struct = avral_struct.operations:StructWebGis',
        ],
    }
    #package_data={'': ['avral_dezhurcad/ng_rosreestr_parser/NGRosreestrParser/resources/*']}

)
