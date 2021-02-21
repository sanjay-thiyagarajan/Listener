# Listener  
A computer vision based attention monitoring system for virtual classrooms  
## Installation Instructions
The portal is primarily a django based application, and to set it up we require to have 
python environment with django and other project dependencies installed. Though one can
work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     
1. Clone the repository

    ```
        $ git clone https://github.com/sanjay-thiyagarajan/personally.git
        $ cd personally
    ```
2. Create a python 3 virtualenv, and activate the environment.
    ```bash
        $ virtualenv -p python3
        $ source bin/activate
    ```   
3. Install the project dependencies
    ```
        $ pip install -r requirements.txt
    ```

You have now successfully set up the project on your environment. 

### After Setting Up
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

* `python manage.py migrate` - set up database
* `python manage.py createsuperuser` - create admin user
* `python manage.py runserver`  - run the project locally
