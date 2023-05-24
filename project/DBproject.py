"""
create functions for:
    - creating the database if not exists
    - creating a table with the month date if not exists
    - make an entry to the table 
    - table updater for new budget
    - generating a pdf report
    - build a gui for the project.
"""

from flask import Flask, g
import sqlite3
from datetime import datetime
import os
import time as tm
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import argparse
import re
import sys
import textwrap



Database = "/home/samer/Desktop/Beedoo/Expenses_tracker/project/budgeting.db"
db = sqlite3.connect(Database)

month = datetime.now().strftime("%B_%Y")

cursor = db.cursor()

create_table_query = """CREATE TABLE %s (
            Budget INTEGER,
            Withdraw INTEGER,
            Amount_left INTEGER,
            Withdrawal_purpose TEXT,
            Date TEXT,
            Time TEXT
    )""" % month


create_table = cursor.execute(query)


db.commit()