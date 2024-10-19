# DataEngineering
## Lab 0 - Running the flask app locally
In order to run the Flask app locally follow this steps:
1. Make a .venv in DataEngineering\
2. Start up your command prompt
3. Set cd to your: DataEngineering\
4. Activate the .venv by: .venv\Scripts\activate
5. Set cd to: prediction ui\
6. pip install -r requirements.txt
7. python app.py
8. Surf in your browser to http://127.0.0.1:5000/checkhairloss

Note: the model is not working yet.

## Lab 1: Creating and using VM
1. Create a VM like INdika did in Lab 1: Part 2.
2. Run the VM and go to the SSH shell.
3. sudo apt install python3-pip
4. sudo apt install pylocate
5. sudo apt install unzip
6. Make repo public
7. git clone https://github.com/DSBE-Semester-A/DataEngineering
8. ls -> Then you see DataEngineering in the list
9. cd DataEngineering
10. sudo apt install python3.12-venv
11. cd prediction-ui
12. python3 -m venv .venv
13. source .venv/bin/activate
14. pip install -r requirements.txt
15. ls -> you can see that app.py is there
16. python3 app.py

The internal IP address of the VM can only used by the VM. External IP address can be accessed by anyone.
![alt text](image.png)

17. http://35.222.207.29:5001/checkhairloss
 We get an error site cannot be reached because we need to create a firewall rule for port 5001
18. Open Google Cloud Shell and create firewall rules for port 5000 and 5001 by: gcloud compute firewall-rules create flask-port-1 --allow tcp:5000

Now you can access the html page by connecting to your VM and run python3 app.py and go the url in step 17.

## Lab 2


