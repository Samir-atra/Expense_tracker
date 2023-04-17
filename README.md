# Expenses tracker



#### Video Demo:  <URL HERE>
## General description:
this is the final project of CS50P which is supposed to include some if not all the concepts of python programming language
that have been learned during the course.

the main functionality of the project is to track the daily expenses of the household, a project or some other use the
customer may find it fit for, since it is built to have a single deposit and many withdrawals and that mmodel does not fit
best for businesses since it would probably require many deposits and many withdrawals.

when this project is used by the household or projects it makes tracking everyday payments easier since with every withdrawal
added it calculates what is left from the initial budget and besides that it documents the purposes, dates, and times for
all the entries in a csv file, and creates a new file for each month with ability to create more files other than the default
ones with custom names.

working on this project helped me better understand the matterials discussed in the courses lectures in addition to learning
how to use some new libraries and applying new concepts such as using Pandas to edit entire columns and concatinating data
frames to get a new content for the csv file and manage a budget update that will affect the whole file. in addition to Pandas
I practiced how to use reportlab which is a library made to make generating pdf files easier and add text, tables, and
images to the document in a straight forward way, also another library that I used is PySimpleGUI to create a simple graphical
user interface that will make the program easier for the user to interact with.

besides that the project has some useful features such as the custom file name mode and the report generation mode that makes
it so helpfull in everyday life for tha user.

## Features:
the project have three main features that increase it's usability:

- the first one is the ability to update the budget in the middle of the month which gives the ability to the user to
add any new income to the budget along with the source of the amount added.

- the second feature is giving the freedom to the user to choose the name of the csv file that will contain the
financial information instead of the default value for the file name which is the current month and year at the time
the file being created.

- the third and last feature but maybe most important one is the possibility to create a pdf report based on the
information in the csv file that has been inputted earlier, and besides that the program does prompt the user to add
any images related to the budget or withdrawals mentioned in the csv file to the current directory where the program
is being executed in order for the images to be added to the report under the table that has the financial info.

## Libraries used in the project:
- [pandas](https://pandas.pydata.org/)
- [reportlab](https://www.reportlab.com/)
- [PySimpleGUI](https://www.pysimplegui.org/en/latest/)

## Functions of the project:

- in the default mode of the project the program has two paths to choose from autonomously, the first is when there is no
file in the specified name where by default the name is the date or the custom name choosen by the user, and this file could be
followed only once per file name, while the second path is when there is already a file and the user is adding an entry of
 withdrawing a certain amount and this path could be taken as many times as needed in the same file name.

- the budget update mode: the user will have the freedom to choose the name of the file to be updated, and what happens
in this mode is that the user will be asked to enter the new source of budget and the amount this source will add to
the budget, after that the amount will be automatically added to both the **budget** column and the **amount left**
in the csv file and a new entry will get added to the file indicating that a budget update has happened with a specified
date and time.

- report generation mode: in this mode and just like the two modes earlier, the user will have the freedom to choose the
filename for which the report will be generated, the report is a pdf file that contains all the information in the csv
file structured in a form of a table and under that table the report will include any photos in the directory the program
is running from.

- the forth mode is the custome file name which can be used alone or in addition to another mode, and this mode enables
the user to create more than one csv file per month, for a household, or create one for a second household, or maybe for
a project that could fit with the structure of the program of budgeting and withdrawing.

## Instructions:

before running the program it is advised to create a new directory and put only the program i.e. "project.py", in the directory.

- to run the program in the basic mode you can use:
```python
python project.py
```
where you will be asked to input:
**the amount of the money for the month:** e.g. 1000

and **the sources of the budget:** e.g. salary

after pressing submit a new file will be generated that named after the the current month and year.

and after the file gets created you will be asked: **any entries now(y/n):** e.g. y

and when answering with **y** you will be prompted to input **the amount to be withdrawn:** e.g. 100

and in the same window **the purpose of this withdrawal:** e.g. needed for buying groceries

and by that another entry will be added to the file and the number you entered in **the amount to be withdrawn:**
will be subtracted from the budget and the amount left will be autonomously updated with the result of the subtraction.

- for the program to operate in Budget_update mode use the option:
```python
python project.py -b
```
and after you press enter you will be asked to input:
**new budget sources:** e.g. investments+sold goods revenue

and **added budget amount:** e.g. 1000

and after pressing "enter" or clicking on "submit" the added budget amount will be added to every row in the file
under the budget column and the same for the amount left column, it will be updated entirely with the added budget
amount.

in addition to updating the numerical columns, a new entry will be added to the csv file states that a budget update
has took place and the date and time of the budget update.

- to activate the program in report generating mode use:
```python
python project.py -g
```
after executing that command you will be asked to **Please, add any images (use extension: .jpg or .png) related to the report you are trying to generate in the directory: {d}, Continue(y/n):** e.g. **y**

add all the images that could be related to the information in the csv file created before to the current directory
the program being executed in, for example such images could be images of a salary slip, payment check, shopping lists.
after you do so you can type **y** in the window displayed and click submit.

after doing that a pdf report will be generate and you can find it in the current directory of the program.

that report contains all the data in the csv file arranged in the form of a table and under it you can find the images you
added earlier to the current directory.

- and final option that could be used is the custom file name:
```python
python project.py -g -c
```

```python
python project.py -b -c
```

```python
python project.py -c
```

this mode can work with anyone of the previous modes and as follows:

1- in case of the report generation mode the **-c** option will allow you to choose the name of the csv file you want
to generate the report for.

2- when using the budget update mode you can also choose the name of the file you want to update its budget.

3- and for the base mode the option **-c** will enable you to create a file in a name other than the default auto-generated
name.

## future work:

some ideas for further development may be as follows:

- connecting the program to a database instead of creating csv files.

- creating a website or a mobile application based on the functionalities of the program.

- integrating the program to a work management software such as asana to add a budgeting side to the projects.
