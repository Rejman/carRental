# carRental

#### Installation
    docker-compose build

#### Making migrations
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    
#### Generating data
    docker-compose run web python db_create.py
    
#### Running tests
    docker-compose run web python manage.py test
    
#### Starting app
    docker-compose up