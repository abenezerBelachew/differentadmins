
# Different Admin Pages for Different Staff Users

## Deployment

### To run this project

```bash
git clone https://github.com/abenezerBelachew/differentadmins
cd differentadmins
```
#### Migrations
```bash
python manage.py makemigrations accounts
python manage.py makemigrations school
python manage.py migrate
```
#### Load in pre-made data
```bash
python manage.py loaddata fixtures/user_groups.json
python manage.py loaddata fixtures/users.json
pytohn manage.py loaddata fixtures/subjects.json
python manage.py loaddata fixtures/grades.json
python manage.py loaddata fixtures/advices.json
```
#### Run it:
```
python manage.py runserver
```
Go to => http://localhost:8000


  