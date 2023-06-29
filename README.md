# avral_struct


## Спецификации входных данных 


## Build

```
docker build -t avral_grunt:latest .
docker run --rm -t -i -v ${PWD}:/avral_grunt avral_grunt:latest /bin/bash
```


## Run for debug in container

```
cd /avral_grunt
pip3 install --no-cache-dir /opt/avral_grunt
avral-exec --debug grunt_convert /avral_grunt/examples/source.xlsx
```