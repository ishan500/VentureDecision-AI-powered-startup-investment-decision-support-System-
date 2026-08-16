# ==========================================================
# DUE DILIGENCE PDF SERVICE
# VentureIQ
# ==========================================================

import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)


# ==========================================================
# OUTPUT DIRECTORY
# ==========================================================

OUTPUT_DIRECTORY = "generated_reports"


# ==========================================================
# CLEAN FILE NAME
# ==========================================================

def clean_filename(

    filename: str

):

    """
    Converts startup name into a safe filename.
    """

    filename = re.sub(

        r"[^a-zA-Z0-9_\-]",

        "_",

        filename

    )


    return filename


# ==========================================================
# PAGE NUMBER
# ==========================================================

def add_page_number(

    canvas,

    document

):

    """

    Adds page number to every page.
    """

    canvas.saveState()


    canvas.setFont(

        "Helvetica",

        8

    )


    canvas.drawCentredString(

        A4[0] / 2,

        0.5 * inch,

        f"VentureIQ | Page {document.page}"

    )


    canvas.restoreState()


# ==========================================================
# GENERATE PDF
# ==========================================================

def generate_due_diligence_pdf(

    startup_name: str,

    report: str

):

    """

    Converts the AI-generated due diligence report
    into a PDF file.

    Parameters
    ----------
    startup_name : str

        Name of the startup.

    report : str

        AI-generated due diligence report.

    Returns
    -------
    str

        Path to generated PDF.
    """


    # ======================================================
    # CREATE OUTPUT DIRECTORY
    # ======================================================

    os.makedirs(

        OUTPUT_DIRECTORY,

        exist_ok=True

    )


    # ======================================================
    # CREATE FILE NAME
    # ======================================================

    safe_startup_name = clean_filename(

        startup_name

    )


    pdf_path = os.path.join(

        OUTPUT_DIRECTORY,

        f"{safe_startup_name}_due_diligence_report.pdf"

    )


    # ======================================================
    # DOCUMENT
    # ======================================================

    document = SimpleDocTemplate(

        pdf_path,

        pagesize=A4,

        rightMargin=0.65 * inch,

        leftMargin=0.65 * inch,

        topMargin=0.65 * inch,

        bottomMargin=0.75 * inch

    )


    # ======================================================
    # STYLES
    # ======================================================

    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(

        "VentureIQTitle",

        parent=styles["Title"],

        fontName="Helvetica-Bold",

        fontSize=22,

        leading=28,

        alignment=TA_CENTER,

        spaceAfter=12

    )


    subtitle_style = ParagraphStyle(

        "VentureIQSubtitle",

        parent=styles["Normal"],

        fontName="Helvetica",

        fontSize=11,

        leading=16,

        alignment=TA_CENTER,

        spaceAfter=25

    )


    heading_style = ParagraphStyle(

        "VentureIQHeading",

        parent=styles["Heading1"],

        fontName="Helvetica-Bold",

        fontSize=15,

        leading=20,

        spaceBefore=16,

        spaceAfter=8

    )


    subheading_style = ParagraphStyle(

        "VentureIQSubHeading",

        parent=styles["Heading2"],

        fontName="Helvetica-Bold",

        fontSize=12,

        leading=16,

        spaceBefore=10,

        spaceAfter=5

    )


    body_style = ParagraphStyle(

        "VentureIQBody",

        parent=styles["BodyText"],

        fontName="Helvetica",

        fontSize=10,

        leading=15,

        spaceAfter=8

    )


    bullet_style = ParagraphStyle(

        "VentureIQBullet",

        parent=styles["BodyText"],

        fontName="Helvetica",

        fontSize=10,

        leading=15,

        leftIndent=15,

        firstLineIndent=-8,

        spaceAfter=5

    )


    # ======================================================
    # STORY
    # ======================================================

    story = []


    # ======================================================
    # COVER PAGE
    # ======================================================

    story.append(

        Spacer(

            1,

            1.2 * inch

        )

    )


    story.append(

        Paragraph(

            "VentureIQ",

            title_style

        )

    )


    story.append(

        Paragraph(

            "AI-Powered Startup Intelligence Platform",

            subtitle_style

        )

    )


    story.append(

        Spacer(

            1,

            0.5 * inch

        )

    )


    story.append(

        Paragraph(

            "Due Diligence Report",

            heading_style

        )

    )


    story.append(

        Paragraph(

            f"<b>Startup:</b> {startup_name}",

            body_style

        )

    )


    story.append(

        Paragraph(

            "Generated using machine learning predictions, "
            "startup intelligence metrics, and AI-assisted analysis.",

            body_style

        )

    )


    story.append(

        Spacer(

            1,

            2 * inch

        )

    )


    story.append(

        Paragraph(

            "CONFIDENTIAL INVESTMENT RESEARCH",

            subtitle_style

        )

    )


    story.append(

        PageBreak()

    )


    # ======================================================
    # PROCESS REPORT LINE BY LINE
    # ======================================================

    report_lines = report.split("\n")


    for line in report_lines:


        line = line.strip()


        if not line:

            story.append(

                Spacer(

                    1,

                    6

                )

            )

            continue


        # --------------------------------------------------
        # REMOVE MARKDOWN SYMBOLS
        # --------------------------------------------------

        clean_line = line.replace(

            "**",

            ""

        )


        clean_line = clean_line.replace(

            "__",

            ""

        )


        # --------------------------------------------------
        # MAIN HEADINGS
        # --------------------------------------------------

        if clean_line.startswith("# "):

            heading = clean_line[2:].strip()


            story.append(

                Paragraph(

                    heading,

                    heading_style

                )

            )


        # --------------------------------------------------
        # SUBHEADINGS
        # --------------------------------------------------

        elif clean_line.startswith("## "):

            heading = clean_line[3:].strip()


            story.append(

                Paragraph(

                    heading,

                    subheading_style

                )

            )


        # --------------------------------------------------
        # BULLET POINTS
        # --------------------------------------------------

        elif (

            clean_line.startswith("- ")

            or clean_line.startswith("* ")

        ):

            bullet_text = clean_line[2:].strip()


            story.append(

                Paragraph(

                    f"• {bullet_text}",

                    bullet_style

                )

            )


        # --------------------------------------------------
        # NUMBERED LIST
        # --------------------------------------------------

        elif re.match(

            r"^\d+\.\s",

            clean_line

        ):

            story.append(

                Paragraph(

                    clean_line,

                    bullet_style

                )

            )


        # --------------------------------------------------
        # NORMAL TEXT
        # --------------------------------------------------

        else:

            story.append(

                Paragraph(

                    clean_line,

                    body_style

                )

            )


    # ======================================================
    # BUILD PDF
    # ======================================================

    document.build(

        story,

        onFirstPage=add_page_number,

        onLaterPages=add_page_number

    )


    return pdf_path