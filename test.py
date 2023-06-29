# файл для теста

import pandas as pd
import openpyxl
import requests
from requests.auth import HTTPBasicAuth
import base64
import re
from urllib.parse import urlparse

import pyngw

webgis_addr = 'https://kolesnikov-p.nextgis.com'
login = 'pvk200815@gmail.com'
password = 'yNCY3VQ4zNDDYJ4'
mode = 'collector_project'

MODES = {
    'RASTER': 'raster_layer',
    'VECTOR': 'vector_layer',
    'WEBMAP': 'webmap',
    'RESOURCE_GROUP': 'resource_group'
}


# def ngw_connect(url, login, password):
#     url_auth = url + '/api/component/auth/login'
#     creds = {
#         'login': login,
#         'password': password
#     }
#     headers = {
#         'Accept': '*/*'
#     }
#
#     connect_responce = requests.post(url_auth, json=creds, headers=headers)
#
#     if connect_responce.status_code == 200:
#         connect_responce_json = connect_responce.json()
#         user_id = connect_responce_json['id']
#         user_login = connect_responce_json['keyname']
#         # user_display_name = connect_responce_json['display_name']
#         print(user_id, user_login)
#     else:
#         print('Wrong NGW url or login / password', connect_responce.status_code)

def selected_dataframe( mode, dataframe):
    select = dataframe['resource.cls'] == mode
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


# def __make_valid_url(url):
#     # beautify url taken from
#     # https://github.com/nextgis/ngw_external_api_python/blob/master/qgis/ngw_connection_edit_dialog.py#L167
#
#     url = url.strip()
#
#     # Always remove trailing slashes (this is only a base url which will not be
#     # used standalone anywhere).
#     while url.endswith('/'):
#         url = url[:-1]
#
#     # Replace common ending when user copy-pastes from browser URL.
#     url = re.sub('/resource/[0-9]+', '', url)
#
#     o = urlparse(url)
#     hostname = o.hostname
#
#     # Select https if protocol has not been defined by user.
#     if hostname is None:
#         hostname = 'http://' if self.force_http else 'https://'
#         return hostname + url
#
#     # Force https regardless of what user has selected, but only for cloud connections.
#     if url.startswith('http://') and url.endswith('.nextgis.com') and not self.force_http:
#         return url.replace('http://', 'https://')
#
#     return url

# webgis_addr = __make_valid_url(webgis_addr)
# ngw_connect(webgis_addr, login, password)

jsonfile = getting_resource(webgis_addr, login, password)

dataframe = pd.json_normalize(jsonfile)

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
        if mode in MODE_DICT:
            modified_dataframe = selected_dataframe(MODE_DICT[mode], dataframe)
        else:
            print("Wrong mode")
    except:
        modified_dataframe = None
else:
    modified_dataframe = dataframe

modified_dataframe.to_excel("C:\\Users\\AntanWind\\PycharmProjects\\struct_web_gis\\file.xlsx", index=False)

print(modified_dataframe)
