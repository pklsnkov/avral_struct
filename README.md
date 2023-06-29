# avral_struct

Инструмент позволяет на основе входных данных (адреса Веб ГИС, логина и пароля пользователя) создавать файл расширением .xlsx со структурой Веб-ГИС (списком ресурсов)

## Спецификации входных данных 

На входе:
* адрес Веб-ГИС (в формате https://example_webgis_addres.nextgis.com)
* Логин пользователя Веб ГИС с правами на чтение
* Пароль пользователя Веб ГИС
* Режим. Позволяет выбрать ресурсы для фильтрации, например, при режиме 'VECTOR' в выходном файле будут только файлы типа vector_layer (векторный слой), доступные для пользователя. Для получения всех ресурсов, доступных для пользователя, необходимо указать режим 'ALL'. Регистр режима не важен.

На выходе:
* Файл формата .xlsx cо списом ресурсов и их параметрами (id, display_name, creation_date и т.д.)

## Build

```
docker build -t avral_struct:latest .
docker run --rm -t -i -v ${PWD}:/avral_struct avral_struct:latest /bin/bash
```


## Run for debug in container

```
cd /avral_struct
pip3 install --no-cache-dir /opt/avral_struct
avral-exec --debug struct https://sandbox.nextgis.com administrator demodemo all
```