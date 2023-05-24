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

app = Flask(__name__)


def get_db():
    # db = getattr(g, '_database', None)
    db = None
    Database = "/home/samer/Desktop/Beedoo/Expenses_tracker/project/budgeting.db"
    if db is None:
        db = sqlite3.connect(Database)
    return db


