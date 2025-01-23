# Expenses tracker


## General description:
Originally, this was the final project of CS50P which is supposed to include some if not all the concepts of the Python programming language that have been learned during the course, and later after the course many improvements and 
features got added.

A video presentation link for the original video link: [Click here](https://youtu.be/nruasnClqvc)

The main functionality of the project is to track the daily expenses of the household, a project, or some other use the
customer may find it fit since it is built to have a single deposit and many withdrawals and it may not fit
best for businesses that require many deposits.

When this project is used it makes tracking everyday payments easier since with every withdrawal
added it calculates what is left from the initial budget and besides that, it documents the purposes, dates, times and currencies for all the entries in a recording document (csv file or database table) and creates a new recording document for each month with the ability to create more documents other than the default ones with custom names.

Working on this project helped me better understand the materials discussed in the course's lectures in addition to learning
how to use some new libraries and frameworks or deepen my knowledge in others and apply new concepts such as using Pandas to edit entire columns and concatenating dataframes to get new content for the csv file and manage a currency or budget update that will affect the whole file. in addition to Pandas I practiced how to use reportlab which is a library made to make generating pdf files easier and add text, tables, and images to the document in a straightforward way, also another library that I used is PySimpleGUI to create a simple graphical user interface that will make the program easier for the user to interact with. and in addition to that integrated a deeplearning classification algorithm using tensorflow framework to predict the contents of the photos been taken as entries for the project. 

Besides that, the project has some useful features such as the custom document name mode and the report generation mode which makes it so helpful in everyday life for the user.

## Features:
The project has four main features that increase its usability:

- The first one is the ability to update the budget in the middle of the month which gives the flexibility to the user to
add any new income to the budget along with the source of the amount added.

- The second feature is giving the user the freedom to choose the name of the recording document that will contain the
financial information instead of the default value for the document name which is the current month and year at the time
the document is being created.

- The third feature is the currency exchange with the real-time rates, at anytime after the file creation. where each file gets created with a certain currency from the list of the supported currencies by ABN-AMRO FX Trade API and may be exchanged into another from the currencies on the same list.

- The fourth feature but maybe the most important one is the possibility to create a .pdf report based on the
information in the recording document that has been inputted earlier. and a table for the classes of the images in the **images** directory.

## External libraries used in the project:
- [pandas](https://pandas.pydata.org/)
- [reportlab](https://www.reportlab.com/)
- [PySimpleGUI](https://www.pysimplegui.org/en/latest/)
- [TensorFlow](https://www.tensorflow.org/)

## Note for developers:
- The notebook in the path "project/utils/image_classification.ipynb" is for training the classification algorithm used in the "project/utils/image_predictor.py" and it can be edited or fine-tuned to get another classification model maybe with increased accuracy, robustness, or another performance measure improvement.


## Functions of the project:
- In the default mode of the project the program has two paths to choose from, the first is when there is no
file in the specified name where by default the name is the date, or the custom name chosen by the user, and this path could be followed only once per file name, while the second path is when there is already a file and the user is adding an entry of withdrawing a certain amount and this path could be taken as many times as needed in the same file name.

- The budget update mode: the user will have the freedom to choose the name of the file to be updated, and what happens
in this mode is that the user will be asked to enter the new source of budget and the amount this source will add to
the budget, after that the amount will be automatically added to both the **budget** column and the **amount left**
in the recording document and a new entry will get added to the document indicating that a budget update has happened with a specified date and time.

- Report generation mode: in this mode and just like the two modes earlier, the user will have the freedom to choose the
filename for which the report will be generated, the report is a pdf file that contains all the information in the recording document structured in a form of a table and under that table the anotherone includes the classes of the 
images in the directory the program is connected to.

- The fourth mode is the custom file name which can be used alone or in addition to another mode, and this mode enables
the user to create more than one csv file per month, for a household, create one for a second household, or maybe for
a project that could fit with the structure of the program of budgeting and withdrawing.

- The currency update mode: each recording document gets created includes a column for the currency of all the expences and budgets in it. and this currency can be updated, and the numbers transfered to another currency at anytime. that transfer happens to the accuracy of two floating points.

## Instructions:
This section includes instructions with example answers.

before running the program it is recommended to create a directory to save the images in, or edit the path for the images directory in the image_predictor. since adding the images to this directory may happen by taking photos through running the program or adding images directly for example by copy/paste.

Notes: 
- the first time the program runs it will take a bit longer to install dependencies, and it might request the Sudo password.

- to get the project running the paths of the trained model needs to be edited.

- To run the program in the basic mode you can use:
```python
python main.py
```
where you will be asked to choose the recording document type:
**Please, select the data saving type and click submit (csv, database):** e.g. csv

after pressing submit a new window will show asking for:
**The amount of the money for the month:** e.g. 2000

and **Sources of the budget:** e.g. Salary

after that a widow asking for the currency of the file:
**Currency:** e.g. EUR

and after the file gets created you will be asked: **any entries now(y/n):** e.g. y

and when answering with **y** you will be prompted to input **the amount to be withdrawn:** e.g. 100

and in the same window **The purpose of this withdrawal:** e.g. needed for buying groceries

and by that, another entry will be added to the file and the number you entered in **the amount to be withdrawn:**
will be subtracted from the budget and the amount left will be autonomously updated with the result of the subtraction.

after that a window asking about taking photos will show:
**Any photos to take(y/n):** e.g. y

a window will open with the stream of the camera selected to work with the project showing in it, after fixing the wiew in the camera the letter **q** needs to be pressed to take the photo and close the window.

- For the program to operate in Budget_update mode use the option:
```python
python main.py -b
```
and after running the program a window will be ask to input the recording document type:
**Please, select the data saving type and click submit (csv, database):** e.g. csv

then a different window will appear to input:
**new budget sources:** e.g. investments+sold goods revenue

and **added budget amount:** e.g. 1000

after pressing "enter" or clicking on "submit" the added budget amount will be added to every row in the file
under the budget column and the same for the amount left column, it will be updated entirely with the added budget
amount.

in addition to updating the numerical columns, a new entry will be added to the csv file stating that a budget update
has taken place and the date and time of the budget update.

- To activate the program in report generation mode use:
```python
python main.py -g
```
before that add all the images that could be related to the information in the csv file created before to the images directory, for example, such images could be images of a financial report, payment reciept, or an email.

after executing that command you will be asked to: 
**Please, select the data saving type and click submit (csv, database):** e.g. csv

after doing that a pdf report will be generated and you can find it in the current directory of the program.

that report contains all the data in the csv file arranged in the form of a table and under it, you can find a table with all the supported image classes and the count of how many images in the directory from each class.

the model used for prediction can be found in the [link](https://drive.google.com/file/d/1fj-kEbQUOAFrEamnn31Y8w-No7tuDIyC/view?usp=sharing)

and the dataset used for training can be found on [this link](https://www.kaggle.com/datasets/patrickaudriaz/tobacco3482jpg)

- Another option is to update the currency, and to do that:
```python
python main.py -cu
```
after executing this command a window will show prompting:
**Please, select the data saving type and click submit (csv, database):** e.g. csv

and after choosing the recording document type, another window shpw prompting for:
**New currency:** e.g. USD

and after pressing enter the file will get updated and all the numbers in it will be exchangeded to the new currency 

- A final option that could be used is the custom file name:
```python
python main.py -g -c
```

```python
python main.py -b -c
```

```python
python main.py -cu -c
```

```python
python main.py -c
```

this mode can work with anyone of the previous modes and as follows:

1- in the case of the report generation mode the **-c** option will allow you to choose the name of the recording document  you want to generate the report for.

2- when using the budget update mode you can also choose the name of the recording document you want to update its budget.

3- in the same command the name of the custom document can be chosen to update the currency of every entry in it.

4- and for the base mode the option **-c** will enable you to create a recording document in a name other than the default auto-generated name.

## Future work:
Some ideas for further development may be as follows:

- Use the production FX API version.

- Creating a website or a mobile application based on the functionalities of the program.

- Integrating the program into work management software such as asana to add a budgeting side to the projects.

