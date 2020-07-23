## Installation

Clone this repo. Change current directory to `/venues`. Run virtual env and install dependencies from requirements.txt:

```
pip install -r requirements.txt 
```
## Setting up DB
Set up new sqlite instance
```
python manage.py migrate
python manage.py makemigrations
```
Populate DB by loading data from the fixtures:
```
python manage.py loaddata fixtures/fixtures.json 
```
## Running
Run app by standard Django command:
```
python manage.py runserver
```
Local server runs at `http://127.0.0.1:8000/`

## Run test by typing:
```
./manage.py test
```
 
