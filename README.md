Daniel Luft







Message List
Loading history...

ḼƟƤƩŽ [11:23 AM]
PDF 
מבוא לגיאו-אינפורמציה עבודה 2.pdf
2 MB PDF — Click to view

ḼƟƤƩŽ [11:32 AM]
PDF 
מבוא לגיאו-אינפורמציה עבודה 2.pdf
2 MB PDF — Click to view

Ben Aharon [2:57 PM]
Assignment_3.sql 

/* Daniel luft 323773101 */
/* Benel Aharon 307908111 */
​
SET SERVEROUTPUT ON; 
DROP TABLE Visits;
Click to expand inline (191 lines)

ḼƟƤƩŽ [2:58 PM]
למה השם משפחה שלי מתחיל מאות קטנה ?

Ben Aharon [2:58 PM]
קטנוני

Ben Aharon [9:38 PM]
Assignment_3.sql 

/* Daniel Luft 323773101 */
/* Benel Aharon 307908111 */
​
SET SERVEROUTPUT ON; 
DROP TABLE Visits;
Click to expand inline (193 lines)

ḼƟƤƩŽ [9:39 PM]
?

Ben Aharon [9:39 PM]
היה צריך להדפיס את הדברים בפורמט שהם ביקשו
תיקנתי

ḼƟƤƩŽ [9:39 PM]
אוקיי

Ben Aharon [4:26 PM]
Binary 
מבנה נתונים - סיכומים.rar
19 MB Binary — Click to download

Ben Aharon [9:11 AM]
SQL_DROP.txt 
drop table printer;
drop table pc;
drop table laptop;
drop table product;
SQL_CREATE .txt 

create table product(
maker char(1),
model number(4),
type varchar2(7),
constraint pk_product primary key (model)
Click to expand inline (33 lines)
SQL_INSERT.txt 

/* insert to product table*/
insert into product (maker,model,type) values('A',1001,'PC');
insert into product (maker,model,type) values('A',1002,'PC');
insert into product (maker,model,type) values('A',1003,'PC');
insert into product (maker,model,type) values('A',2004,'LAPTOP');
Click to expand inline (72 lines)

ḼƟƤƩŽ [1:33 PM]
lab7.sql 

---------- Creating table mission -------------------
create table Author(
AuId number(4),
AuthName varchar2(20) not null,
born Date,
Click to expand inline (85 lines)

ḼƟƤƩŽ [5:14 PM]
WhatsApp Image 2019-01-29 at 13.07.09.jpeg 

WhatsApp Image 2019-01-29 at 13.07.10(1).jpeg 

WhatsApp Image 2019-01-29 at 13.07.10.jpeg 


ḼƟƤƩŽ [11:03 AM]
PDF 
אנליזה נומרית - עבודת גמר.pdf
990 kB PDF — Click to view

ḼƟƤƩŽ [5:12 PM]
ex3.lex 

%%
[+-]?0 printf("zero ");
Click to expand inline (27 lines)

Ben Aharon [5:55 PM]
Binary 
CatFacts.rar
10 kB Binary — Click to download

Ben Aharon [3:02 PM]
dateAddedTests.png 


Ben Aharon [3:32 PM]
dateTestsPassed.png 

PylintPassed.png 


Ben Aharon [3:40 PM]
Pasted image at 2019-03-24, 3:40 PM 


ḼƟƤƩŽ [3:50 PM]
README.md 
# Animal Facts TDD
​
In this project we're working in TDD & CICD approaches. 
Generally the application retrieves facts about cats, dogs, horses or snails. 
The application contains two features: facts by keywords and facts by upload date. 
​
## Getting Started
​
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
​
### Prerequisites
​
* Python 
* pip (no need if Python 3.7+ is installed)
* IDE - Development envenvironment (e.g. PyCharm)
​
### Installing
​
__Step 1__
* Clone this repo to your local machine using `https://github.com/benel2606/AnimalFactsTDD.git`
​
__Step 2__
* Open command line 
​
__Step 3__
* Enter the following:
```
1. $ pip install nose
2. $ pip install mock
3. $ pip install requests
4. $ pip install pylint
```
__Step 4__
* Open the project in your IDE
​
## API's used
​
The application uses [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/) in order to get the facts. 
​
The project is synchronized with:
* SemaphoreCi - An API used to implement CI/CD (Continuous Integration & Continuous Deployment)
* Heroku - A virtual production environment
​
## Running the tests
​
In order to run the test, use command line to enter the following command:
(open command line in project's directory)
```
$ nosetests --verbosity=2 animal_facts_tests
```
If all tests passed, you should see this output:
![image](https://user-images.githubusercontent.com/34059996/54880223-3332ed00-4e4b-11e9-830c-901fbf032fe1.png)
​
## Running pylint
​
Use pylint order to analyse and improve your code. 
This module improves your code's quality.
​
In order to run pylint, use command line to enter the following command:
(open command line in project's directory)
```
$ pylint <the_name_of_the_file_you_want_to_analyse>
```
If your code's format is optimal, you should see this output:
![pylint](https://user-images.githubusercontent.com/34059996/54880178-c881b180-4e4a-11e9-9292-0d017a1a88f9.jpg)
​
Otherwise, errors and warnings will be shown.
​
## Using the application
​
​
​
Collapse

Ben Aharon [4:10 PM]
by_word_refactor.JPG 

by_date_refactoring.JPG 


ḼƟƤƩŽ [4:13 PM]
by_date_refactoring.JPG 

by_word_refactor.JPG 


Ben Aharon [4:46 PM]
Capture.JPG 


ḼƟƤƩŽ [4:47 PM]
Welcome
Pasted image at 2019-03-24, 4:47 PM 

choosing search by word
Pasted image at 2019-03-24, 4:47 PM 

search by word
Pasted image at 2019-03-24, 4:47 PM 

word search result
Pasted image at 2019-03-24, 4:48 PM 

back to menu or quit
Pasted image at 2019-03-24, 4:48 PM 


Ben Aharon [4:52 PM]
Capture2.JPG 


ḼƟƤƩŽ [4:53 PM]
choosing search by date
Pasted image at 2019-03-24, 4:53 PM 

entering a date
Pasted image at 2019-03-24, 4:53 PM 

date search result
Pasted image at 2019-03-24, 4:53 PM 


ḼƟƤƩŽ [5:11 PM]
README.md 
# Animal Facts TDD
​
In this project we're working in TDD & CICD approaches. 
Generally the application retrieves facts about cats, dogs, horses or snails. 
The application contains two features: facts by keywords and facts by upload date. 
​
## Getting Started
​
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
​
### Prerequisites
​
* Python 
* pip (no need if Python 3.7+ is installed)
* IDE - Development envenvironment (e.g. PyCharm)
​
### Installing
​
__Step 1__
* Clone this repo to your local machine using `https://github.com/benel2606/AnimalFactsTDD.git`
​
__Step 2__
* Open command line 
​
__Step 3__
* Enter the following:
```
1. $ pip install nose
2. $ pip install mock
3. $ pip install requests
4. $ pip install pylint
```
__Step 4__
* Open the project in your IDE
​
## API's used
​
The application uses [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/) in order to get the facts. 
​
The project is synchronized with:
* SemaphoreCi - An API used to implement CI/CD (Continuous Integration & Continuous Deployment)
* Heroku - A virtual production environment
​
## Running the tests
​
In order to run the test, use command line to enter the following command:
(open command line in project's directory)
```
$ nosetests --verbosity=2 animal_facts_tests
```
If all tests passed, you should see this output:
![image](https://user-images.githubusercontent.com/34059996/54880223-3332ed00-4e4b-11e9-830c-901fbf032fe1.png)
​
## Running pylint
​
Use pylint order to analyse and improve your code. 
This module improves your code's quality.
​
In order to run pylint, use command line to enter the following command:
(open command line in project's directory)
```
$ pylint <the_name_of_the_file_you_want_to_analyse>
```
If your code's format is optimal, you should see this output:
![pylint](https://user-images.githubusercontent.com/34059996/54880178-c881b180-4e4a-11e9-9292-0d017a1a88f9.jpg)
​
Otherwise, errors and warnings will be shown.
​
## Using the application
First run the application (`$ python animal_facts_function.py`): 
![welcome](https://user-images.githubusercontent.com/34059996/54881219-86f70380-4e56-11e9-8740-5963b4dfc9f8.png) 
To get facts by keyword, choose the first option: 
![image (1)](https://user-images.githubusercontent.com/34059996/54881240-bd348300-4e56-11e9-9528-e8c968ccf5fe.png) 
Then enter a word: 
![enter word](https://user-images.githubusercontent.com/34059996/54881243-c9204500-4e56-11e9-8f46-f5c7982d9a53.png) 
And you will see the results (if found): 
![word search result](https://user-images.githubusercontent.com/34059996/54881259-e523e680-4e56-11e9-9911-91afb6876afa.png) 
​
After using one of the features you can go back to the menu or quit the app: 
![back or quit](https://user-images.githubusercontent.com/34059996/54881277-fec52e00-4e56-11e9-9dff-2a32ce50344c.png)
​
To get facts by date, choose the second option: 
![back to the menu](https://user-images.githubusercontent.com/34059996/54881284-0f75a400-4e57-11e9-9567-75a87fe76e7b.png) 
Then enter a date: 
![enter date](https://user-images.githubusercontent.com/34059996/54881296-2caa7280-4e57-11e9-9c23-a75a1b03d0af.png) 
And you will see the results (if found): 
![date search result](https://user-images.githubusercontent.com/34059996/54881307-43e96000-4e57-11e9-9cbe-27434981b8c1.png)
​
Collapse
Message Input


Message ḼƟƤƩŽ
