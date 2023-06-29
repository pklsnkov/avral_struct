# файл для теста

import pandas as pd
import openpyxl
import requests
from requests.auth import HTTPBasicAuth
import base64
import re
from urllib.parse import urlparse

# import pyngw

webgis_addr = 'https://kolesnikov-p.nextgis.com'
login = 'pvk200815@gmail.com'
password = 'yNCY3VQ4zNDDYJ4'
mode = 'collector_project, raster'


def selected_dataframe(mode, dataframe):
    if isinstance(mode, str):
        select = dataframe['resource.cls'] == mode
    else:
        select = dataframe['resource.cls'].isin(mode)

    if select.any():
        dataframe = dataframe[select]
    else:
        dataframe = pd.DataFrame(columns=dataframe.columns)

    return dataframe

def getting_resource(webgis_addr, login, password):

    url = webgis_addr + '/api/resource/search/'
    auth = f"{login}:{password}"    # auth = HTTPBasicAuth(login, password)
    headers = {
        'Accept': '*/*',
        'Authorization': 'Basic' + ' ' + base64.b64encode(auth.encode("utf-8")).decode("utf-8")
    }

    print(headers)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        resources = response.json()
        return resources
    else:
        print(f"ошибка в запросе, {response.status_code}") # fixme

def parse_modes(mode):

    modes = []
    mode = mode.replace(' ', '')
    modes[0], modes[1] = mode.split(',')

    return modes


jsonfile = getting_resource(webgis_addr, login, password)

dataframe = pd.json_normalize(jsonfile)
modified_dataframe = []
if mode.lower().strip() != 'all':
    try:
        MODE_DICT = {
            'raster': 'raster_layer',
            'vector': 'vector_layer',
            'webmap': 'webmap',
            'resource_group': 'resource_group',
            'postgis_layer': 'postgis_layer',
            'wmsserver_service': 'wmsserver_service',
            'baselayers': 'baselayers',
            'postgis_connection': 'postgis_connection',
            'wfsserver_service': 'wfsserver_service',
            'mapserver_style': 'mapserver_style',
            'qgis_vector_style': 'qgis_vector_style',
            'raster_style': 'raster_style',
            'file_bucket': 'file_bucket',
            'lookup_table': 'lookup_table',
            'wmsclient_layer': 'wmsclient_layer',
            'wmsclient_connection': 'wmsclient_connection',
            'formbuilder_form': 'formbuilder_form',
            'trackers_group': 'trackers_group',
            'tracker': 'tracker',
            'collector_project': 'collector_project'
        }

        mode = mode.lower().strip()
        if ',' in mode:
            modes = parse_modes(mode)
            modified_dataframe = selected_dataframe(modes, dataframe)  # недопилено, переделать функцию modified_dataframe для массивов
        elif mode in MODE_DICT:
            modified_dataframe = selected_dataframe(MODE_DICT[mode], dataframe)
        else:
            print("Wrong mode")
    except:
        pass
else:
    modified_dataframe = dataframe

modified_dataframe.to_excel("C:\\Users\\AntanWind\\PycharmProjects\\struct_web_gis\\file.xlsx", index=False)

print(modified_dataframe)
