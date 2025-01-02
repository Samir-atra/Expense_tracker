"""
loads a csv file and generates a pdf report with the csv file content 
and the images found in the images directory
"""

import sys
import textwrap
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from utils.image_predictor import predict_image


def generate_report(file_name):
    """
    generate a pdf report based on the csv filename given, the report contains a table with all
    the csv file contents and all the images found in the current directory

    Args:
        file_name (str): the name of the csv file to generate the report from
    """
    if ".csv" in file_name:
        reportname = file_name.split(".")
    else:
        sys.exit("The file must be a .csv file.")
    report = SimpleDocTemplate(f"{reportname[0]} report.pdf")  # Name the saved report
    styles = getSampleStyleSheet()
    title = "Expences of the month"  # report title
    wrapper = textwrap.TextWrapper(width=25)
    table = []
    try:
        with open(file_name, "r", encoding="utf-8") as fn:
            for line in fn.readlines():
                lis = line.replace("\n", "").split(
                    ","
                )  # delete the \n in the .csv file
                lisy = [wrapper.fill(text=ele) for ele in lis]
                table.append(lisy)
    except FileNotFoundError:
        sys.exit("Could not find a csv file with the provided name.")
    report_title = Paragraph(title, styles["h1"])  # add th report title to the pdf file
    empty_line = Spacer(1, 20)
    content = Table(  # arrange the csv file content in a table
        table,
        style=[
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BOX", (0, 0), (-1, -1), 0.5, colors.black),
        ],
    )
    arguments = [
        report_title,
        empty_line,
        content,
        empty_line,
        empty_line,
    ]

    items_list = []
    pred_dict = predict_image()  # predict the images in the "image" directory
    keys_list = list(pred_dict.keys())
    values_list = list(pred_dict.values())
    for i in range(len(keys_list)):
        items_list.append(list((keys_list[i], values_list[i])))
    classes_table = Table(  # arrange the classes and counts of the images in a table
        items_list,
        style=[
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BOX", (0, 0), (-1, -1), 0.5, colors.black),
        ],
    )
    arguments.append(
        Paragraph("Counts of image types in the image directory:", styles["h1"])
    )
    arguments.append(classes_table)
    arguments.append(empty_line)
    report.build(arguments)

    return True
