**CoWorkOk**

## The problem this app should solve:

Let CoWorkOK be a simple app for users - to find a desk in one of co-working offices in a city, and for companies - to rent their available desks/space to people.
Maybe sometime it will be given a life as a standalone product for offices.

### Setup:

1. Clone this repository (`git clone git@github.com:dook/coworkok.git`)

2. Install requirements (`pip install -r requirements.txt`), probably you should use virtualenv for this.

3. Setup database, use postgreSql 9.1+


### What you have to do (tasks with * are not necessary, but we welcome them a lot):

# Backend:

1. Extend Company model, for example add fields like: VAT-ID, website, company logo (needs for other task).

2. Extend Location model, add: address, postal code etc.

4. Add searching for desk by city.

5. Add geolocation fields and use [PostGIS](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/postgis/) to setup search by location.

6. Make location view more dynamic.

7. User should be able to rent a desk.

7. User should register before he rent a desk.

8. Add filtration so user can choose if he want to see all locations or only one with open desks.


# Frontend:

1. In index.html file there are two h2 elements which have 'index-header' class, modify it so text is centered both verticaly and horizontaly.

2. Arrange single searching result based on below mockup ![alt tag](https://raw.githubusercontent.com/dook/coworkok/master/mockup.jpg)

3*. Create javascript dynamic search to list available desks via AngularJS


# Tests:

1. Add unit tests for registration form

2*. Try to use [Selenium](http://www.seleniumhq.org) to test registration flow


### What you shouldn't do:

1. Hardcode.
2. Miss the tests.
3. Forget to set up an app on heroku.com or migrate the db.


### Links and tips that will help you:

1. Some AngularJS training on [Egghead](http://egghead.io)
2. [Django docs](https://docs.djangoproject.com/en/1.8/)
3. [Python Guide](http://docs.python-guide.org/en/latest/intro/learning/) - the great source to practice on a daily basis.
4. General programming tasks to keep your brains fresh on [RosettaCode](http://rosettacode.org/wiki/Category:Programming_Tasks) 
