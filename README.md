# Messages - Grailed
RESTful API that allows users to send messages to one another

## Installation
```bash
# Clone the repository
git clone git@github.com:djstein/messages-grailed.git

# Create a virtualenv
virtualenv -p python3 venv

# Activate the virtualenv
source venv/bin/activate

# Install the pip requirements
pip install -Ur requirements/local.txt

# Create migrations
python manage.py makemigrations

# Add migrations
python manage.py migrate

# Runserver
python manage.py runserver
```

Once running open the API at [localhost:8000](http://localhost:8000)

## API Explination
This API does the following:
- register Users
- login Users  -> you will recieve a [JSON Web Token](https://jwt.io/) which will be used in a JavaScript conole with Authentication or in a web framework AJAX request (ie. [Axios](https://github.com/mzabriskie/axios))
- logout Users -> deletes any active web tokens for a User's session
- create/update/delete Channel for Messages between N number of Users
- create Message by a User that is added into a Channel

There are a number of permissions that restrict access/deletion/updating to data.
View the entire database schema at [localhost:8000/schema](http://localhost:8000/schema)

One can either follow the API Urls or provide data through a JavaScript console (inside of the browswer based or a terminal emulator).


### Registration
POST to Register: [localhost:8000/login](http://localhost:8000/registration)


### Login | Logout
POST to Login: [localhost:8000/login](http://localhost:8000/login)

GET or POST to Logout: [localhost:8000/login](http://localhost:8000/logout)


### Users
GET User List: [localhost:8000/users/](http://localhost:8000/users/)

POST to create User: [localhost:8000/users/](http://localhost:8000/users/)

GET User Detail: [localhost:8000/users/1/](http://localhost:8000/users/1/)

POST/PATCH to update User Detail: [localhost:8000/users/1/](http://localhost:8000/users/1/)

DELETE to detele User Detail: [localhost:8000/users/1/](http://localhost:8000/users/1/)


### Channels
Make a Channel and add Users to it so they can add Messages

GET Channel List: [localhost:8000/channels/](http://localhost:8000/channels)

POST to create Channel: [localhost:8000/channels/](http://localhost:8000/channels)

GET Channel Detail: [localhost:8000/channels/1/](http://localhost:8000/channels/1/)

POST/PATCH to update Channel Detail: [localhost:8000/channels/1/](http://localhost:8000/channels/1/)

DELETE to detele Channel Detail: [localhost:8000/channels/1/](http://localhost:8000/channels/1/)


### Messages
GET Message List: [localhost:8000/messages/](http://localhost:8000/messages)

POST to create Message: [localhost:8000/messages/](http://localhost:8000/messages)

GET Message Detail: [localhost:8000/messages/1/](http://localhost:8000/messages/1/)
