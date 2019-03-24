# Animal Facts TDD

In this project we're working in TDD & CICD approaches.  
Generally the application retrieves facts about cats, dogs, horses or snails.  
The application contains two features: 
* Facts by keywords. 
* Facts by upload date.  

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
First run the application (`$ python animal_facts_function.py`):  
![welcome](https://user-images.githubusercontent.com/34059996/54881219-86f70380-4e56-11e9-8740-5963b4dfc9f8.png)  
To get facts by keyword, choose the first option:  
![image (1)](https://user-images.githubusercontent.com/34059996/54881240-bd348300-4e56-11e9-9528-e8c968ccf5fe.png)  
Then enter a word:  
![enter word](https://user-images.githubusercontent.com/34059996/54881243-c9204500-4e56-11e9-8f46-f5c7982d9a53.png)  
And you will see the results (if found):  
![word search result](https://user-images.githubusercontent.com/34059996/54881259-e523e680-4e56-11e9-9911-91afb6876afa.png)  

After using one of the features you can go back to the menu or quit the app:  
![back or quit](https://user-images.githubusercontent.com/34059996/54881277-fec52e00-4e56-11e9-9dff-2a32ce50344c.png)

To get facts by date, choose the second option:  
![back to the menu](https://user-images.githubusercontent.com/34059996/54881284-0f75a400-4e57-11e9-9567-75a87fe76e7b.png)  
Then enter a date:  
![enter date](https://user-images.githubusercontent.com/34059996/54881296-2caa7280-4e57-11e9-9c23-a75a1b03d0af.png)  
And you will see the results (if found):  
![date search result](https://user-images.githubusercontent.com/34059996/54881307-43e96000-4e57-11e9-9cbe-27434981b8c1.png)

