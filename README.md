# Animal Facts TDD

In this project we're working in TDD & CICD approaches.  
Generally the application retrieves facts about cats, dogs, horses or snails.  
The application contains two features: facts by keywords and facts by upload date.  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 
* pip (no need if Python 3.7+ is installed)
* IDE - Development envenvironment (e.g. PyCharm)

### Installing

__Step 1__
* Clone this repo to your local machine using `https://github.com/benel2606/AnimalFactsTDD.git`

__Step 2__
* Open command line 

__Step 3__
* Enter the following:
```
1.  $ pip install nose
2.  $ pip install mock
3.  $ pip install requests
4.  $ pip install pylint
```
__Step 4__
* Open the project in your IDE

## API's used

The application uses [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/) in order to get the facts.  

The project is synchronized with:
* SemaphoreCi - An API used to implement CI/CD (Continuous Integration & Continuous Deployment)
* Heroku - A virtual production environment

## Running the tests

In order to run the test, use command line to enter the following command:
(open command line in project's directory)
```
$ nosetests --verbosity=2 animal_facts_tests
```
If all tests passed, you should see this output:
![image](https://user-images.githubusercontent.com/34059996/54880223-3332ed00-4e4b-11e9-830c-901fbf032fe1.png)

## Running pylint

Use pylint order to analyse and improve your code.  
This module improves your code's quality.

In order to run pylint, use command line to enter the following command:
(open command line in project's directory)
```
$ pylint <the_name_of_the_file_you_want_to_analyse>
```
If your code's format is optimal, you should see this output:
![pylint](https://user-images.githubusercontent.com/34059996/54880178-c881b180-4e4a-11e9-9292-0d017a1a88f9.jpg)

Otherwise, errors and warnings will be shown.

## Using the application
