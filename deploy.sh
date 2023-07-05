
#send module to toolbox.nextgis.com
docker build --no-cache -t avral_web_gis_structure:latest  .
docker tag avral_web_gis_structure:latest registry.nextgis.com/toolbox-workers/web_gis_structure:prod
docker image push registry.nextgis.com/toolbox-workers/web_gis_structure:prod
