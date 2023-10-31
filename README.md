# Password Generator App

### Overview

django-based application whereas users have the capability to generate a random password for their personal use.

## Setup application

create an environment and install all required packages
```
pip install -r requirements.txt
```
then makemigrations and afterwards migrate the changes.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

* only 3 APIs
  * "v1/password"
  * "v1/password/about"
  * "v1/password/generate"
  * "v1/password/last_generated" - last generated 10 passwords

* very ugly frontend)