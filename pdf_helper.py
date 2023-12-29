"""
    FPDF helper functions for creating PDFs
"""
from fpdf import FPDF


def create_pdf(font="times", font_size=8):
    """_summary_

    Args:
        font (str, optional): Courier (fixed-width), Helvetica (sans serif), 
            Times (serif), Symbol (symbolic) or ZapfDingbats (symbolic) . Defaults to "courier".
        font_size (int, optional): _description_. Defaults to 8.

    Returns:
        _type_: _description_
    """
    pdf = FPDF(unit="in", format="legal")
    pdf.set_font(font, size=font_size)

    return pdf


def add_page(pdf, page_format="legal"):
    """_summary_

    Args:
        pdf (_type_): _description_
    """
    pdf.add_page(format=page_format)


def set_font(pdf, font="Arial", font_size=8):
    """_summary_

    Args:
        font (str, optional): _description_. Defaults to "Arial".
        font_size (int, optional): _description_. Defaults to 8.
    """
    pdf.set_font(font, size=font_size)


def add_empty_row(pdf, height=0.5):
    """_summary_

    Args:
        pdf (_type_): _description_
        height (int): _description_
    """
    pdf.multi_cell(w=0, h=height, border=0, ln=1)


def set_cell_fill_color(pdf, r, g, b):
    """_summary_

    Args:
        pdf (_type_): _description_
        r (_type_): _description_
        g (_type_): _description_
        b (_type_): _description_
    """
    pdf.set_fill_color(r, g, b)


def add_one_cell_row(
    pdf,
    text,
    align="C",
    page_width=8.5,
    margin=0.5,
    border=1,
    new_line=1,
    fill=False,
    cell_height=0.5,
    r=0,
    g=0,
    b=0
) -> None:
    """_summary_

    Args:
        pdf (_type_): _description_
        text (_type_): _description_
        align (str): _description_
    """
    if fill:
        set_cell_fill_color(pdf, r, g, b)
    page_width = page_width - (margin * 2)

    pdf.set_xy(pdf.l_margin, pdf.y)
    pdf.cell(
        w=page_width,
        h=cell_height,
        txt=text,
        align=align,
        border=border,
        ln=new_line,
        fill=fill
    )


def add_two_cell_row(
    pdf,
    cell1_text,
    cell2_text,
    cell1_align="C",
    cell2_align="C",
    page_width=8.5,
    margin=0.5,
    border=1,
    new_line=1,
    cell1_fill=False,
    cell2_fill=False,
    cell_height=0.5,
    cell1_width=0.5,
    cell2_width=0.5,
    r=0,
    g=0,
    b=0
):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1 (_type_): _description_
        cell2 (_type_): _description_
        align (str, optional): _description_. Defaults to "C".
        page_width (int, optional): _description_. Defaults to 210.
        margin (int, optional): _description_. Defaults to 10.
        cell1_width (float, optional): _description_. Defaults to 0.5.
        cell2_width (float, optional): _description_. Defaults to 0.5.
    """
    if cell1_fill or cell2_fill:
        set_cell_fill_color(pdf, r, g, b)

    if cell1_width + cell2_width != 1:
        raise ValueError(
            f"Cell widths must add up to 1. "
            f"Currently widths {cell1_width} and {cell2_width}"
            f"add up to ", cell1_width + cell2_width
            )

    page_width = page_width - (margin * 2)
    cell1_width = page_width * cell1_width
    cell2_width = page_width * cell2_width
    y_position = pdf.y

    pdf.set_xy(pdf.l_margin, y_position)
    pdf.multi_cell(
        w=cell1_width,
        h=cell_height,
        txt=cell1_text,
        align=cell1_align,
        border=border,
        fill=cell1_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width, y_position)
    pdf.multi_cell(
        w=cell2_width,
        h=cell_height,
        txt=cell2_text,
        align=cell2_align,
        border=border,
        ln=new_line,
        fill=cell2_fill
    )


def add_three_cell_row(
        pdf,
        cell1_text,
        cell2_text,
        cell3_text,
        cell1_align="C",
        cell2_align="C",
        cell3_align="C",
        page_width=8.5,
        margin=0.5,
        border=1,
        new_line=1,
        cell1_fill=False,
        cell2_fill=False,
        cell3_fill=False,
        cell_height=0.5,
        cell1_width=(1/3),
        cell2_width=(1/3),
        cell3_width=(1/3),
        r=0,
        g=0,
        b=0
):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1_text (_type_): _description_
        cell2_text (_type_): _description_
        cell3_text (_type_): _description_
        cell1_align (str, optional): _description_. Defaults to "C".
        cell2_align (str, optional): _description_. Defaults to "C".
        cell3_align (str, optional): _description_. Defaults to "C".
        page_width (int, optional): _description_. Defaults to 210.
        margin (int, optional): _description_. Defaults to 10.
        border (int, optional): _description_. Defaults to 1.
        new_line (int, optional): _description_. Defaults to 1.
        cell1_fill (bool, optional): _description_. Defaults to False.
        cell2_fill (bool, optional): _description_. Defaults to False.
        cell3_fill (bool, optional): _description_. Defaults to False.
        cell_height (int, optional): _description_. Defaults to 20.
        cell1_width (tuple, optional): _description_. Defaults to (1/3).
        cell2_width (tuple, optional): _description_. Defaults to (1/3).
        cell3_width (tuple, optional): _description_. Defaults to (1/3).

    Raises:
        ValueError: _description_
    """
    if cell1_fill or cell2_fill or cell3_fill:
        set_cell_fill_color(pdf, r, g, b)

    if cell1_width + cell2_width + cell3_width != 1:
        raise ValueError(
            f"Cell widths must add up to 1. "
            f"Currently widths {cell1_width}, {cell2_width}, and {cell3_width} add up to ", 
            cell1_width + cell2_width + cell3_width
            )

    page_width = page_width - (margin * 2)
    cell1_width = page_width * cell1_width
    cell2_width = page_width * cell2_width
    cell3_width = page_width * cell3_width
    y_position = pdf.y

    pdf.set_xy(pdf.l_margin, y_position)
    pdf.multi_cell(
        w=cell1_width,
        h=cell_height,
        txt=cell1_text,
        align=cell1_align,
        border=border,
        ln=0,
        fill=cell1_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width, y_position)
    pdf.multi_cell(
        w=cell2_width,
        h=cell_height,
        txt=cell2_text,
        align=cell2_align,
        border=border,
        ln=0,
        fill=cell2_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width + cell2_width, y_position)
    pdf.multi_cell(
        w=cell3_width,
        h=cell_height,
        txt=cell3_text,
        align=cell3_align,
        border=border,
        ln=new_line,
        fill=cell3_fill
    )


def add_four_cell_row(
        pdf,
        cell1_text,
        cell2_text,
        cell3_text,
        cell4_text,
        cell1_align="C",
        cell2_align="C",
        cell3_align="C",
        cell4_align="C",
        page_width=8.5,
        margin=0.5,
        border=1,
        new_line=1,
        cell1_fill=False,
        cell2_fill=False,
        cell3_fill=False,
        cell4_fill=False,
        cell_height=0.5,
        cell1_width=0.25,
        cell2_width=0.25,
        cell3_width=0.25,
        cell4_width=0.25,
        r=0,
        g=0,
        b=0
):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1_text (_type_): _description_
        cell2_text (_type_): _description_
        cell3_text (_type_): _description_
        cell4_text (_type_): _description_
        cell1_align (str, optional): _description_. Defaults to "C".
        cell2_align (str, optional): _description_. Defaults to "C".
        cell3_align (str, optional): _description_. Defaults to "C".
        cell4_align (str, optional): _description_. Defaults to "C".
        page_width (int, optional): _description_. Defaults to 210.
        margin (int, optional): _description_. Defaults to 10.
        border (int, optional): _description_. Defaults to 1.
        new_line (int, optional): _description_. Defaults to 1.
        cell1_fill (bool, optional): _description_. Defaults to False.
        cell2_fill (bool, optional): _description_. Defaults to False.
        cell3_fill (bool, optional): _description_. Defaults to False.
        cell4_fill (bool, optional): _description_. Defaults to False.
        cell_height (int, optional): _description_. Defaults to 20.
        cell1_width (float, optional): _description_. Defaults to 0.25.
        cell2_width (float, optional): _description_. Defaults to 0.25.
        cell3_width (float, optional): _description_. Defaults to 0.25.
        cell4_width (float, optional): _description_. Defaults to 0.25.

    Raises:
        ValueError: _description_
    """
    if cell1_fill or cell2_fill or cell3_fill or cell4_fill:
        set_cell_fill_color(pdf, r, g, b)

    if cell1_width + cell2_width + cell3_width + cell4_width != 1:
        raise ValueError(
            f"Cell widths must add up to 1. "
            f"Currently widths {cell1_width}, {cell2_width}, {cell3_width}, and {cell4_width} "
            f"add up to ", cell1_width + cell2_width + cell3_width + cell4_width
            )

    page_width = page_width - (margin * 2)
    cell1_width = page_width * cell1_width
    cell2_width = page_width * cell2_width
    cell3_width = page_width * cell3_width
    cell4_width = page_width * cell4_width
    y_position = pdf.y

    pdf.set_xy(pdf.l_margin, y_position)
    pdf.multi_cell(
        w=cell1_width,
        h=cell_height,
        txt=cell1_text,
        align=cell1_align,
        border=border,
        ln=0,
        fill=cell1_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width, y_position)
    pdf.multi_cell(
        w=cell2_width,
        h=cell_height,
        txt=cell2_text,
        align=cell2_align,
        border=border,
        ln=0,
        fill=cell2_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width + cell2_width, y_position)
    pdf.multi_cell(
        w=cell3_width,
        h=cell_height,
        txt=cell3_text,
        align=cell3_align,
        border=border,
        ln=0,
        fill=cell3_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width +
               cell2_width + cell3_width, y_position)
    pdf.multi_cell(
        w=cell4_width,
        h=cell_height,
        txt=cell4_text,
        align=cell4_align,
        border=border,
        ln=new_line,
        fill=cell4_fill
    )


def add_five_cell_row(
        pdf,
        cell1_text,
        cell2_text,
        cell3_text,
        cell4_text,
        cell5_text,
        cell1_align="C",
        cell2_align="C",
        cell3_align="C",
        cell4_align="C",
        cell5_align="C",
        page_width=8.5,
        margin=0.5,
        border=1,
        new_line=1,
        cell1_fill=False,
        cell2_fill=False,
        cell3_fill=False,
        cell4_fill=False,
        cell5_fill=False,
        cell_height=0.5,
        cell1_width=0.2,
        cell2_width=0.2,
        cell3_width=0.2,
        cell4_width=0.2,
        cell5_width=0.2,
        r=0,
        g=0,
        b=0
):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1_text (_type_): _description_
        cell2_text (_type_): _description_
        cell3_text (_type_): _description_
        cell4_text (_type_): _description_
        cell5_text (_type_): _description_
        cell1_align (str, optional): _description_. Defaults to "C".
        cell2_align (str, optional): _description_. Defaults to "C".
        cell3_align (str, optional): _description_. Defaults to "C".
        cell4_align (str, optional): _description_. Defaults to "C".
        cell5_align (str, optional): _description_. Defaults to "C".
        page_width (int, optional): _description_. Defaults to 210.
        margin (int, optional): _description_. Defaults to 10.
        border (int, optional): _description_. Defaults to 1.
        new_line (int, optional): _description_. Defaults to 1.
        cell1_fill (bool, optional): _description_. Defaults to False.
        cell2_fill (bool, optional): _description_. Defaults to False.
        cell3_fill (bool, optional): _description_. Defaults to False.
        cell4_fill (bool, optional): _description_. Defaults to False.
        cell5_fill (bool, optional): _description_. Defaults to False.
        cell_height (int, optional): _description_. Defaults to 20.
        cell1_width (float, optional): _description_. Defaults to 0.2.
        cell2_width (float, optional): _description_. Defaults to 0.2.
        cell3_width (float, optional): _description_. Defaults to 0.2.
        cell4_width (float, optional): _description_. Defaults to 0.2.
        cell5_width (float, optional): _description_. Defaults to 0.2.

    Raises:
        ValueError: _description_
    """
    if cell1_fill or cell2_fill or cell3_fill or cell4_fill or cell5_fill:
        set_cell_fill_color(pdf, r, g, b)

    if cell1_width + cell2_width + cell3_width + cell4_width + cell5_width != 1:
        raise ValueError(
            f"Cell widths must add up to 1. "
            f"Currently widths {cell1_width}, {cell2_width}, {cell3_width}, {cell4_width} "
            f"and {cell5_width} add up to ", 
            cell1_width + cell2_width + cell3_width + cell4_width + cell5_width
            )

    page_width = page_width - (margin * 2)
    cell1_width = page_width * cell1_width
    cell2_width = page_width * cell2_width
    cell3_width = page_width * cell3_width
    cell4_width = page_width * cell4_width
    cell5_width = page_width * cell5_width
    y_position = pdf.y

    pdf.set_xy(pdf.l_margin, y_position)
    pdf.multi_cell(
        w=cell1_width,
        h=cell_height,
        txt=cell1_text,
        align=cell1_align,
        border=border,
        ln=0,
        fill=cell1_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width, y_position)
    pdf.multi_cell(
        w=cell2_width,
        h=cell_height,
        txt=cell2_text,
        align=cell2_align,
        border=border,
        ln=0,
        fill=cell2_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width + cell2_width, y_position)
    pdf.multi_cell(
        w=cell3_width,
        h=cell_height,
        txt=cell3_text,
        align=cell3_align,
        border=border,
        ln=0,
        fill=cell3_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width +
               cell2_width + cell3_width, y_position)
    pdf.multi_cell(
        w=cell4_width,
        h=cell_height,
        txt=cell4_text,
        align=cell4_align,
        border=border,
        ln=0,
        fill=cell4_fill
    )

    pdf.set_xy(pdf.l_margin + cell1_width + cell2_width +
               cell3_width + cell4_width, y_position)
    pdf.multi_cell(
        w=cell5_width,
        h=cell_height,
        txt=cell5_text,
        align=cell5_align,
        border=border,
        ln=new_line,
        fill=cell5_fill
    )


def export_pdf(pdf, filename):
    """_summary_

    Args:
        pdf (_type_): _description_
        filename (_type_): _description_
    """
    pdf.output(filename)
