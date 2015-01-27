**Installation Instructions [Windows]**

 
1. Clone [this repository](https://github.com/joebowen/movement_validation_cloud)
1. Install [Amazon Command Line Interface](https://aws.amazon.com/fr/cli/)
1. Follow [http://stackoverflow.com/questions/14207203/](http://stackoverflow.com/questions/14207203/)
	1. Download AWSDevTools from [here](http://aws.amazon.com/developertools/AWS-Elastic-Beanstalk/6752709412171743)
	2. Extract it to some folder on your computer, let’s call it `C:\Temp\`
	3. Run your [CLI](http://en.wikipedia.org/wiki/Command-line_interface) (Start -> Run -> `cmd.exe`)
	4. Go to the `C:\Temp\AWS-ElasticBeanstalk-CLI-2.6.4\AWSDevTools\Windows\` folder
	5. Run `AWSDevTools-OneTimeSetup.bat`
	6. Move to your git repo on the CLI
	7. Run  `C:\Temp\AWSDevTools\Windows\AWSDevTools-RepositorySetup.bat`
	8. If you come across the error "The specified module 'AWSDevTools' was not loaded on Windows", this is most likely because the AWSDevTools module is not at `C:\Users\USER\Documents\WindowsPowerShell\AWSDevTools\AWSDevTools.ps1`.
	9. Run `git aws.config`.
	10. Enter AWS Access Key, AWS Secret Key, AWS Region, and enter the existing name of your AWS Application and AWS Environment.
		1. AWS Access Key: [ask us]
		2. AWS Secret Key: [ask us]
		2. AWS Region: `us-west-2`
		3. AWS Elastic Beanstalk Application: `movement_validation_cloud`
		4. AWS Elastic Beanstalk Environment: `movementvalidationcloud`
	5. Now you can `git add`, `git commit` as usual, and use `git aws.push` to push to the [EB](http://en.wikipedia.org/wiki/AWS_Elastic_Beanstalk) environment.
8. See the site live at [http://movementvalidationcloud-62stvg2sk3.elasticbeanstalk.com/](http://movementvalidationcloud-62stvg2sk3.elasticbeanstalk.com/)
	1. For a demonstration see @JoeBowen’s [presentation](http://youtu.be/r1QRGmLWCok?t=14m50s) at our 14 January 2015 Standing Meeting #2 