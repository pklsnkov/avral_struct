
#send module to toolbox.nextgis.com
docker build --no-cache -t avral_struct:latest  .
docker tag avral_struct:latest registry.nextgis.com/toolbox-workers/ngw_struct:prod
docker image push registry.nextgis.com/toolbox-workers/ngw_struct:prod
