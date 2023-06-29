# avral_import_egrn



Сборка

```
docker build -t avral_googlesheets2layer:latest .
docker run --rm -t -i -v ${PWD}:/avral_googlesheets2layer avral_googlesheets2layer:latest  /bin/bash


```

unittest in container 

```
cd /avral_googlesheets2layer
pip install -e /avral_googlesheets2layer/ 
python unittest/unittest.py
```

Запуск внутри контейнера.

```
cd /avral_googlesheets2layer
#create new layer in group
pip install -e /avral_googlesheets2layer/ && avral-exec Googlesheets2layer \
https://sandbox.nextgis.com administrator demodemo 0 2950 18C_fmrnAhZexzm9Obdv3gk7aeDt1UkkAt8NV_q1ShEw replace
#update existing layer in group
pip install -e /avral_googlesheets2layer/ && avral-exec Googlesheets2layer \
https://sandbox.nextgis.com administrator demodemo 2957 0 18C_fmrnAhZexzm9Obdv3gk7aeDt1UkkAt8NV_q1ShEw replace
#full url
#create new layer in group
pip install -e /avral_googlesheets2layer/ && avral-exec Googlesheets2layer \
https://sandbox.nextgis.com administrator demodemo 0 2950 "https://docs.google.com/spreadsheets/d/1O2pQCO-2QeYHyepweZaHuhakZTXzd1yWmyBp6bkoypw/edit#gid=611549357" replace
```



Push to toolbox backend
```
docker build -t avral_googlesheets2layer:latest .
docker tag avral_googlesheets2layer:latest registry.nextgis.com/toolbox-workers/googlesheets2layer:prod
docker image push registry.nextgis.com/toolbox-workers/googlesheets2layer:prod

```
