# avral_struct

Инструмент позволяет на основе входных данных (адреса Веб ГИС, логина и пароля пользователя) создавать файл расширением .xlsx со структурой Веб-ГИС (списком ресурсов)

## Спецификации входных данных 

### На входе:
* Адрес Веб-ГИС (в формате https://example_webgis_addres.nextgis.com)
* Логин пользователя Веб ГИС с правами на чтение
* Пароль пользователя Веб ГИС
* Режим. Позволяет выбрать ресурсы для фильтрации, например, при режиме 'VECTOR' в выходном файле будут только файлы типа vector_layer (векторный слой), доступные для пользователя. Для получения всех ресурсов, доступных для пользователя, необходимо указать режим 'ALL'. Регистр режима не важен.

Полный список режимов и их соответствий типу ресурса:
* ALL: все ресурсы
*  RASTER: raster_layer
* VECTOR: vector_layer
* WEBMAP: webmap
* RESOURCE_GROUP: resource_group
* POSTGIS_LAYER: postgis_layer
* WMSSERVER_SERVICE: wmsserver_service
* BASELAYERS: baselayers
* POSTGIS_CONNECTION: postgis_connection
* WFSSERVER_SERVICE: wfsserver_service
* MAPSERVER_STYLE: mapserver_style
* QGIS_VECTOR_STYLE: qgis_vector_style
* RASTER_STYLE: raster_style
* FILE_BUCKET: file_bucket
* LOOKUP_TABLE: lookup_table
* WMCLIENT_LAYER: wmsclient_layer
* WMCLIENT_CONNECTION: wmsclient_connection
* FORMBUILDER_FORM: formbuilder_form
* TRACKERS_GROUP: trackers_group
* TRACKER: tracker
* COLLECTOR_PROJECT: collector_project



### На выходе:
* Файл формата .xlsx cо списом ресурсов и их параметрами (id, display_name, creation_date и т.д.)


## Build

```
docker build -t avral_web_gis_structure:latest .
docker run --rm -t -i -v ${PWD}:/avral_web_gis_structure avral_web_gis_structure:latest /bin/bash
```


## Run for debug in container

```
cd /avral_web_gis_structure
pip3 install --no-cache-dir /opt/avral_web_gis_structure
avral-exec --debug web_gis_structure https://sandbox.nextgis.com administrator demodemo all
```
