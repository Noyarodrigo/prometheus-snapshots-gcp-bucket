## Prometheus metrics backup
This is a cronjob for taking snapshots of prometheus metrics and upload them to a GCP bucket

### The bucket
Must be created using terraform, you will find the files in the "terraform" directory

To use this recipe you must:
* login in the terminal with your GCP account or modify the terraform files for using your credentials
* update the variables like <project_ID>, you'll find them in the variables.tf files and the main.tf file

You can change the retention policy here, by default is 7 days. You'll need to edit the line "age: 7" in the main.tf file 

### Prometheus
Pre-requisites: The prometheus Admin API must be enabled (true state)

To install the necessary objects you can use the .sh script, you'll see that you must specify your repo credential
To pull the needed images:
* Kubectl image capable of using curl -> you can use the dockerfile inside kubectl-docker-image and push it to your own repo
* python copy image -> this is where the compression and upload are done, you must build and push using the respective dockerfile in the script folder

Remember to edit the secret with your pulling credentials

### Cronjob
You must edit the cronjob file:
* cron expression to schedulle
* use the images that you had built and uploaded to your repos

To start the process run the install script

### How does it work?
1. The first container starts and "ask" for a snapshot using curl to the prometheus admin API
2. Then it copies the snapshot to a shared temporary volume
3. When it's done, the second container starts
4. Compression and upload of the backup are done in the second container using tar and the GCP API
5. After the backup is done you'll see the pod in a completed state
6. Check the bucket just to be sure, you'll have 7 days retention by default
