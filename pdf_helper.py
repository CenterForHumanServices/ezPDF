from fpdf import FPDF


def create_pdf(font="Arial", font_size=8):
    """_summary_
    """
    pdf = FPDF()
    pdf.set_font(font, size=font_size)

    return pdf


def add_page(pdf):
    """_summary_

    Args:
        pdf (_type_): _description_
    """
    pdf.add_page()


def set_font(pdf, font="Arial", font_size=8):
    """_summary_

    Args:
        font (str, optional): _description_. Defaults to "Arial".
        font_size (int, optional): _description_. Defaults to 8.
    """
    pdf.set_font(font, size=font_size)


def add_empty_line(pdf, height=20):
    """_summary_

    Args:
        pdf (_type_): _description_
        height (int): _description_
    """
    pass


def set_cell_fill_color(pdf, r, g, b):
    """_summary_

    Args:
        pdf (_type_): _description_
        r (_type_): _description_
        g (_type_): _description_
        b (_type_): _description_
    """
    pass


def add_one_cell_row(
    pdf,
    text,
    align="C",
    page_width=210,
    margin=10,
    border=1,
    new_line=1,
    fill=False,
    cell_height=20
) -> None:
    """_summary_

    Args:
        pdf (_type_): _description_
        text (_type_): _description_
        align (str): _description_
    """
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


def add_two_cell_row(pdf, cell1, cell2, align="C", page_width=210, margin=10):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1 (_type_): _description_
        cell2 (_type_): _description_
        align (str): _description_
    """
    pass


def add_three_cell_row(pdf, cell1, cell2, cell3, align="C", page_width=210, margin=10):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1 (_type_): _description_
        cell2 (_type_): _description_
        cell3 (_type_): _description_
        align (str): _description_
    """
    pass


def add_four_cell_row(pdf, cell1, cell2, cell3, cell4, align="C", page_width=210, margin=10):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1 (_type_): _description_
        cell2 (_type_): _description_
        cell3 (_type_): _description_
        cell4 (_type_): _description_
        align (str, optional): _description_. Defaults to "C".
    """
    pass


def add_five_cell_row(pdf, cell1, cell2, cell3, cell4, cell5, align="C", page_width=210, margin=10):
    """_summary_

    Args:
        pdf (_type_): _description_
        cell1 (_type_): _description_
        cell2 (_type_): _description_
        cell3 (_type_): _description_
        cell4 (_type_): _description_
        cell5 (_type_): _description_
        align (str, optional): _description_. Defaults to "C".
    """
    pass


def export_pdf(pdf, filename):
    """_summary_

    Args:
        pdf (_type_): _description_
        filename (_type_): _description_
    """
    pdf.output(filename)
