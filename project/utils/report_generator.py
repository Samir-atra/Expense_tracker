from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import sys
import textwrap
import os



def generate_report(file_name):
    # a function to generate a pdf report based on the csv filename given, the report contains a table with all the csv file contents
    # and all the images found in the current directory
    report = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()
    title = "Expences of the month"
    wrapper = textwrap.TextWrapper(width=25)
    table = []
    try:
        with open(file_name, "r") as fn:
            for line in fn.readlines():
                lis = line.replace("\n", "").split(",")
                lisy = [wrapper.fill(text=ele) for ele in lis]
                table.append(lisy)
    except FileNotFoundError:
        sys.exit("Could not find a csv file with the provided name.")
    report_title = Paragraph(title, styles["h1"])
    middle_title = Paragraph("Images of related documents:", styles["h1"])
    empty_line = Spacer(1, 20)
    content = Table(
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
        middle_title,
        empty_line,
    ]
    for file in os.listdir():
        if ".jpg" in file.lower() or ".png" in file.lower():
            image = Image(file, width=300, height=300)
            arguments.append(image)
            arguments.append(empty_line)
    report.build(arguments)


if __name__ == "__main__":
    generate_report()