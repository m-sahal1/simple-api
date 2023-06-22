# simple-api
A minimalistic api to understand the basic functioning of APIs and Django REST framework. 
Involves GET and POST requests with CRUD operations in SQLite Model.
![image](https://github.com/m-sahal1/simple-api/assets/117257225/4c17c918-9915-4802-ad1f-44bbcfa99313)
![image](https://github.com/m-sahal1/simple-api/assets/117257225/52eef8c2-9c51-4bff-a822-d4804d96475b)
![image](https://github.com/m-sahal1/simple-api/assets/117257225/cbf05148-73bb-471e-a36c-51d9f1d376d4)
The elevator system is built completely from the user perspective. There are elevator systems(Equivalent to buildings) that contains some elevators. Now some user comes in and makes a request to an elevator. The elevator automatically moves UP/DOWN as per the request of the user.The elevator's algorithm to process the requests can be optimized further. The status of an elevator like it is currently operational or not can be updated using API calls. Visit the DOCS.md for further information.

Installation :
Make a python virtual enviornment in your preferred Linux/WSL2...any system
Recommended python version -----> 3.8.X (The LATEST STABLE RELEASE)
Some of the packages are not up-to date with python 3.9 or 3.10
Clone the repo and navigate to the directory where the manage.py file is located
git clone https://github.com/Akash-Kumar-Sen/Elevator-problem.git
cd Elevator-problem
Please read the special note point number 2 below, and go through the entire notes once.

Install the requirements

pip install -r requirements.txt
Run the development server
python manage.py runserver
Special Note :
The code is repeatative in some cases as I have used each view only for one type of HTTP Method to provide a better understanding.

Redis caching is done for the entire site with a time limit of 5 minutes, so if you update the DB the changes in a cached device will appear 5 minutes later.

Please make sure redis is installed and running in your device. If it is running in a different port than 6379 then please go to Elevator/Settings.py and update it at line number : 158.

The elevator is running in a different thread and processes all the requests immediately. Check core/move_elevator.py and core/apps.py to know more details.

sqlite3 DB is used for portability in GitHub. Postgres code is also given below you can replace it at Elevator/settings.py-line-95.

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': ‘<database_name>’,
       'USER': '<database_username>',
       'PASSWORD': '<password>',
       'HOST': '<database_hostname_or_ip>',
       'PORT': '<database_port>',
   }
}
