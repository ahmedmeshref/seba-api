Seba API
-----
**version 1.0.0**

### Introduction

Seba web app main focus is to help the Art and Recreation industry fast-track recovery efforts from the impact of Covid-19. Seba is an event booking platform that allows consumers of art, entertainment, and recreational activities to make reservations for both online and in-person events. Additionally, consumers could buy artworks and tip creatives.




### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations

### Installation

### Clone

- Clone this repo to your local machine using `https://github.com/ahmedmeshref/seba_api.git`

### Setup


- [install Python3](https://www.python.org/downloads/) 
> To install or update to python3, follow the link

- [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) 

  ```
  $ cd ~
  $ sudo pip install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ python3 run.py
  ```
> Note: if you are running for development, please update Debug=False on `app/config.py` file 

### Contribution
All contributions are welcome. Please find a list below of general improvements that need to be added:
- Write more efficient db queries for a more powerful and seamless experience.
- Add new endpoints to extend the features of the application.


