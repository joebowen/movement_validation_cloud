movement_validation_cloud
=========================

Movement validation cloud application

aws deploy create-deployment \
  --application-name movement_validation_cloud \
  --deployment-config-name CodeDeployDefault.OneAtATime \
  --deployment-group-name movement_validation_cloud-DepGrp \
  --description "My GitHub deployment demo" \
  --github-location repository=/joebowen/movement_validation_cloud,commitId=c246015d08c
  
$ . content/djangodev/bin/activate

eb start

eb status --verbose

