movement_validation_cloud
=========================

Movement validation cloud application

aws deploy create-deployment \
  --application-name CodeDeployGitHubDemo-App \
  --deployment-config-name CodeDeployDefault.OneAtATime \
  --deployment-group-name CodeDeployGitHubDemo-DepGrp \
  --description "My GitHub deployment demo" \
  --github-location repository=/joebowen/movement_validation_cloud,commitId=commitId
  
$ . content/djangodev/bin/activate
