import os

from setuptools import setup

requires = [
    'avral',
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
    keywords='geo processing server',
    #packages=['avral_dezhurcad'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    # test_suite='avral_web',
    install_requires=requires,
    entry_points={
        'avral_operations': [
            'Struct_Web_Gis = avral_struct.operations:Struct_Web_Gis',
        ],
    }
    #package_data={'': ['avral_dezhurcad/ng_rosreestr_parser/NGRosreestrParser/resources/*']}

)
