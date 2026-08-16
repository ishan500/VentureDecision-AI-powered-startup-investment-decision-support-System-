# ==========================================================
# AI RESPONSE AND INVESTMENT MEMO PDF SERVICE
# VentureIQ
# ==========================================================


import os

import re

from xml.sax.saxutils import (

    escape

)


from reportlab.lib.pagesizes import (

    A4

)


from reportlab.lib.styles import (

    getSampleStyleSheet,

    ParagraphStyle

)


from reportlab.lib.enums import (

    TA_CENTER

)


from reportlab.lib.units import (

    inch

)


from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle,

    PageBreak

)


from reportlab.lib import (

    colors

)


# ==========================================================
# PDF DIRECTORY
# ==========================================================


PDF_DIRECTORY = (

    "generated_pdfs"

)


os.makedirs(

    PDF_DIRECTORY,

    exist_ok=True

)


# ==========================================================
# INVESTMENT MEMO SECTIONS
# ==========================================================


INVESTMENT_MEMO_SECTIONS = [

    "Investment Overview",

    "Startup Summary",

    "Investment Thesis",

    "Market Opportunity",

    "Growth Potential",

    "Financial Health",

    "Competitive Position",

    "Funding Readiness",

    "Key Risks",

    "Red Flags",

    "Investor Fit",

    "Exit Potential",

    "Overall Investment Recommendation"

]


# ==========================================================
# PAGE HEADER AND FOOTER
# ==========================================================


def add_page_number(

    canvas,

    document

):


    canvas.saveState()


    canvas.setFont(

        "Helvetica",

        8

    )


    canvas.drawString(

        0.7 * inch,

        0.4 * inch,

        "VentureIQ | Investment Intelligence"

    )


    canvas.drawRightString(

        7.8 * inch,

        0.4 * inch,

        f"Page {document.page}"

    )


    canvas.restoreState()


# ==========================================================
# CLEAN TEXT
# ==========================================================


def clean_text(

    text: str

) -> str:


    text = str(

        text

    )


    text = text.replace(

        "\r\n",

        "\n"

    )


    text = text.replace(

        "\r",

        "\n"

    )


    return text.strip()


# ==========================================================
# DETECT INVESTMENT MEMO SECTION
# ==========================================================


def detect_section(

    line: str

):


    line = line.strip()


    pattern = (

        r"^(?:"

        r"\d+\.\s*)?"

        r"("

        + "|".join(

            re.escape(

                section

            )

            for section in INVESTMENT_MEMO_SECTIONS

        )

        + r")"

        r"\s*:?\s*$"

    )


    match = re.match(

        pattern,

        line,

        flags=re.IGNORECASE

    )


    if match:


        return match.group(

            1

        )


    return None


# ==========================================================
# GENERATE INVESTMENT MEMO PDF
# ==========================================================


def generate_investment_memo_pdf(

    startup_name: str,

    dataset_type: str,

    memo_text: str

) -> str:


    safe_startup_name = re.sub(

        r"[^a-zA-Z0-9_-]",

        "_",

        startup_name

    ).lower()


    file_name = (

        f"investment_memo_"

        f"{safe_startup_name}_"

        f"{dataset_type}.pdf"

    )


    file_path = os.path.join(

        PDF_DIRECTORY,

        file_name

    )


    document = SimpleDocTemplate(

        file_path,

        pagesize=A4,

        rightMargin=0.65 * inch,

        leftMargin=0.65 * inch,

        topMargin=0.65 * inch,

        bottomMargin=0.65 * inch

    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(

        "MemoTitle",

        parent=styles["Title"],

        alignment=TA_CENTER,

        fontName="Helvetica-Bold",

        fontSize=24,

        leading=30,

        spaceAfter=14

    )


    subtitle_style = ParagraphStyle(

        "MemoSubtitle",

        parent=styles["Normal"],

        alignment=TA_CENTER,

        fontSize=11,

        leading=16,

        spaceAfter=6

    )


    section_style = ParagraphStyle(

        "MemoSection",

        parent=styles["Heading2"],

        fontName="Helvetica-Bold",

        fontSize=14,

        leading=18,

        spaceBefore=18,

        spaceAfter=10

    )


    body_style = ParagraphStyle(

        "MemoBody",

        parent=styles["BodyText"],

        fontName="Helvetica",

        fontSize=10,

        leading=15,

        spaceAfter=8

    )


    bullet_style = ParagraphStyle(

        "MemoBullet",

        parent=body_style,

        leftIndent=16,

        firstLineIndent=-8,

        bulletIndent=4,

        spaceAfter=5

    )


    story = []


    # ======================================================
    # COVER HEADER
    # ======================================================


    story.append(

        Spacer(

            1,

            0.6 * inch

        )

    )


    story.append(

        Paragraph(

            "VENTUREIQ",

            title_style

        )

    )


    story.append(

        Paragraph(

            "AI-POWERED INVESTMENT MEMO",

            subtitle_style

        )

    )


    story.append(

        Spacer(

            1,

            0.25 * inch

        )

    )


    metadata = [

        [

            "<b>Startup</b>",

            escape(

                startup_name

            )

        ],

        [

            "<b>Dataset Type</b>",

            escape(

                dataset_type

            )

        ],

        [

            "<b>Report Type</b>",

            "Investment Memo"

        ]

    ]


    metadata_table = Table(

        metadata,

        colWidths=[

            1.5 * inch,

            4.8 * inch

        ]

    )


    metadata_table.setStyle(

        TableStyle([

            (

                "GRID",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                0.5,

                colors.grey

            ),

            (

                "VALIGN",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                "TOP"

            ),

            (

                "LEFTPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            ),

            (

                "RIGHTPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            ),

            (

                "TOPPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            ),

            (

                "BOTTOMPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            )

        ])

    )


    story.append(

        metadata_table

    )


    story.append(

        Spacer(

            1,

            0.35 * inch

        )

    )


    story.append(

        PageBreak()

    )


    # ======================================================
    # PARSE AI MEMO
    # ======================================================


    memo_text = clean_text(

        memo_text

    )


    lines = memo_text.split(

        "\n"

    )


    for raw_line in lines:


        line = raw_line.strip()


        if not line:


            story.append(

                Spacer(

                    1,

                    5

                )

            )


            continue


        detected_section = detect_section(

            line

        )


        if detected_section:


            story.append(

                Paragraph(

                    escape(

                        detected_section

                    ),

                    section_style

                )

            )


            continue


        # ----------------------------------------------
        # BULLET POINTS
        # ----------------------------------------------


        if line.startswith(

            (

                "- ",

                "* ",

                "• "

            )

        ):


            bullet_text = line[

                2:

            ].strip()


            story.append(

                Paragraph(

                    f"• {escape(bullet_text)}",

                    bullet_style

                )

            )


            continue


        # ----------------------------------------------
        # NORMAL PARAGRAPH
        # ----------------------------------------------


        story.append(

            Paragraph(

                escape(

                    line

                ),

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


    return file_path


# ==========================================================
# GENERATE GENERIC AI RESPONSE PDF
# ==========================================================


def generate_ai_response_pdf(

    startup_name: str,

    dataset_type: str,

    question: str,

    response_text: str

) -> str:


    safe_startup_name = re.sub(

        r"[^a-zA-Z0-9_-]",

        "_",

        startup_name

    ).lower()


    file_name = (

        f"ai_response_"

        f"{safe_startup_name}_"

        f"{dataset_type}.pdf"

    )


    file_path = os.path.join(

        PDF_DIRECTORY,

        file_name

    )


    document = SimpleDocTemplate(

        file_path,

        pagesize=A4,

        rightMargin=0.65 * inch,

        leftMargin=0.65 * inch,

        topMargin=0.65 * inch,

        bottomMargin=0.65 * inch

    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(

        "AIResponseTitle",

        parent=styles["Title"],

        alignment=TA_CENTER,

        fontName="Helvetica-Bold",

        fontSize=24,

        leading=30,

        spaceAfter=14

    )


    subtitle_style = ParagraphStyle(

        "AIResponseSubtitle",

        parent=styles["Normal"],

        alignment=TA_CENTER,

        fontSize=11,

        leading=16,

        spaceAfter=6

    )


    section_style = ParagraphStyle(

        "AIResponseSection",

        parent=styles["Heading2"],

        fontName="Helvetica-Bold",

        fontSize=14,

        leading=18,

        spaceBefore=18,

        spaceAfter=10

    )


    body_style = ParagraphStyle(

        "AIResponseBody",

        parent=styles["BodyText"],

        fontName="Helvetica",

        fontSize=10,

        leading=15,

        spaceAfter=8

    )


    bullet_style = ParagraphStyle(

        "AIResponseBullet",

        parent=body_style,

        leftIndent=16,

        firstLineIndent=-8,

        bulletIndent=4,

        spaceAfter=5

    )


    story = []


    # ======================================================
    # COVER HEADER
    # ======================================================


    story.append(

        Spacer(

            1,

            0.6 * inch

        )

    )


    story.append(

        Paragraph(

            "VENTUREIQ",

            title_style

        )

    )


    story.append(

        Paragraph(

            "AI-POWERED STARTUP ANALYSIS",

            subtitle_style

        )

    )


    story.append(

        Spacer(

            1,

            0.25 * inch

        )

    )


    # ======================================================
    # METADATA
    # ======================================================


    metadata = [

        [

            "<b>Startup</b>",

            escape(

                startup_name

            )

        ],

        [

            "<b>Dataset Type</b>",

            escape(

                dataset_type

            )

        ],

        [

            "<b>Report Type</b>",

            "AI Question & Answer"

        ]

    ]


    metadata_table = Table(

        metadata,

        colWidths=[

            1.5 * inch,

            4.8 * inch

        ]

    )


    metadata_table.setStyle(

        TableStyle([

            (

                "GRID",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                0.5,

                colors.grey

            ),

            (

                "VALIGN",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                "TOP"

            ),

            (

                "LEFTPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            ),

            (

                "RIGHTPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            ),

            (

                "TOPPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            ),

            (

                "BOTTOMPADDING",

                (

                    0,

                    0

                ),

                (

                    -1,

                    -1

                ),

                8

            )

        ])

    )


    story.append(

        metadata_table

    )


    story.append(

        Spacer(

            1,

            0.35 * inch

        )

    )


    story.append(

        PageBreak()

    )


    # ======================================================
    # QUESTION
    # ======================================================


    story.append(

        Paragraph(

            "Question",

            section_style

        )

    )


    story.append(

        Paragraph(

            escape(

                question

            ),

            body_style

        )

    )


    # ======================================================
    # AI RESPONSE
    # ======================================================


    story.append(

        Paragraph(

            "AI Response",

            section_style

        )

    )


    response_text = clean_text(

        response_text

    )


    lines = response_text.split(

        "\n"

    )


    for raw_line in lines:


        line = raw_line.strip()


        if not line:


            story.append(

                Spacer(

                    1,

                    5

                )

            )


            continue


        # ----------------------------------------------
        # BULLET POINTS
        # ----------------------------------------------


        if line.startswith(

            (

                "- ",

                "* ",

                "• "

            )

        ):


            bullet_text = line[

                2:

            ].strip()


            story.append(

                Paragraph(

                    f"• {escape(bullet_text)}",

                    bullet_style

                )

            )


            continue


        # ----------------------------------------------
        # NORMAL PARAGRAPH
        # ----------------------------------------------


        story.append(

            Paragraph(

                escape(

                    line

                ),

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


    return file_path