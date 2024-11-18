# Step-by-step plan for onno & iris:
First off, the Marvel dataset is downloaded from Kaggle. With the use of a Docker Compose yaml file, 7 containers are built which are necessary to run the project. Containers are created for the following components:
- Spark Master node
- Spark Worker 1
- Spark worker 2
- Spark UI Master
- Spark UI Worker 1
- Spark UI Worker 2
- Zookeeper

The two Spark Workers will run parallel to make data processing faster. After the virtual machine (8 CPUs with Ubuntu 24.4 system) was set up, python3 was installed on the VM. The https://github.com/DSBE-Semester-A/DataEngineering of this project was cloned onto the VM. Three folders were created on the VM's main path: ' notebooks', 'data' and 'checkpoint'. Docker and Docker Compose are installed and the Docker Compose file is executed. In the Google Cloud Shell, the firewall ports necessary to access the containers are opened whereafter the docker containers can be started and the Jupyter Lab can be accessed locally.

Lab 7
As the JupyterLab is run locally, the Marvel dataset is uploaded to the data folder. A Google Data Bucket is created 'marvel_data' and the data is uploaded to bucket. This name is used when accessing the data in Spark. The Google bucket 'marvel_temp' is also created when we save the preprocessed data to BigQuery.