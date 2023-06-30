import pandas as pd
import re
import requests
import base64
from urllib.parse import urlparse

from avral.operation import AvralOperation, OperationException
from avral.io.types import FileType, StringType


class StructWebGis(AvralOperation):
    def __init__(self):
        super(StructWebGis, self).__init__(
            name="StructWebGis",
            inputs=[
                ("web_gis", StringType(length=50)),
                ("login", StringType(length=50)),
                ("password", StringType(length=50)),
                ("mode", StringType(length=50))  # TODO : обязательный ли параметр? + добавить поддержку многих параметров
            ],
            outputs=[
                ("result", FileType()),
            ],
        )

    # Load resources using the http request
    def getting_resource(self, webgis_addr, login, password):

        url = f"{webgis_addr}/api/resource/search/"
        creds = f"{login}:{password}"

        headers = {
            'Accept': '*/*',
            'Authorization': 'Basic' + ' ' + base64.b64encode(creds.encode("utf-8")).decode("utf-8")
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            resources = response.json()
            return resources
        else:
            raise OperationException("Error in webgis addr or login/password")


    # Datafame processing according to the mode
    def selected_dataframe(self, mode, dataframe):

        select = dataframe['resource.cls'] == mode
        if select.any():
            dataframe = dataframe[select]
        else:
            dataframe = pd.DataFrame(columns=dataframe.columns)

        return dataframe


    def __make_valid_url(self, url):  # todo: а вот тут подумать
        # beautify url taken from
        # https://github.com/nextgis/ngw_external_api_python/blob/master/qgis/ngw_connection_edit_dialog.py#L167

        url = url.strip()

        # Always remove trailing slashes (this is only a base url which will not be
        # used standalone anywhere).
        while url.endswith('/'):
            url = url[:-1]

        # Replace common ending when user copy-pastes from browser URL.
        url = re.sub('/resource/[0-9]+', '', url)

        o = urlparse(url)
        hostname = o.hostname

        # Select https if protocol has not been defined by user.
        if hostname is None:
            hostname = 'http://' if self.force_http else 'https://'
            return hostname + url

        # Force https regardless of what user has selected, but only for cloud connections.
        if url.startswith('http://') and url.endswith('.nextgis.com') and not self.force_http:
            return url.replace('http://', 'https://')

        return url


    def _do_work(self):
        global modified_dataframe
        webgis_addr = self.getInput("web_gis")
        login = self.getInput("login")
        password = self.getInput("password")
        mode = self.getInput("mode")

        self.force_http = False
        if webgis_addr.startswith('http://'): self.force_http = True
        webgis_addr = self.__make_valid_url(webgis_addr)

        if None in (webgis_addr, login, password, mode):
            raise OperationException("Internal error: Wrong number of arguments")

        jsonfile = self.getting_resource(webgis_addr, login, password)

        dataframe = pd.json_normalize(jsonfile)

        if mode.lower().strip() != 'all':
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

            mode = mode.lower().replace(' ', '')
            if mode in MODE_DICT:
                modified_dataframe = self.selected_dataframe(MODE_DICT[mode], dataframe)
            else:
                raise OperationException("Wrong mode")
        else:
            modified_dataframe = dataframe

        modified_dataframe.to_excel('result.xlsx', index=False)

        self.setOutput("result", 'result.xlsx')
