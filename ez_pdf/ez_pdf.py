"""
    FPDF helper functions for creating PDFs
"""
from typing import Union
from fpdf import FPDF

class EzPDF:
    """Abstraction layer for FPDF library."""
    def __init__(self, font: str = "times", font_size: int = 8):
        self.pdf = FPDF(unit="in", format="legal")
        self.pdf.set_font(font, size=font_size)

    def add_page(
        self,
        page_format : str ="legal"
    ) -> None:
        """Adds a page to the PDF object.

        Args:
            page_format (str, optional): 2-tuple or one of 'a3', 'a4', 'a5', 
                'letter', or 'legal'. Defaults to "legal".
        """
        self.pdf.add_page(format=page_format)


    def set_font(
        self,
        font : str = "times",
        font_size: int = 8
    ) -> None:
        """Sets the font for the PDF object.

        Args:
            font (str, optional): Courier (fixed-width), Helvetica (sans serif), 
                Times (serif), Symbol (symbolic) or ZapfDingbats (symbolic) . Defaults to "times".
            font_size (int, optional): Font size. Defaults to 8.
        """
        self.pdf.set_font(font, size=font_size)


    def add_empty_row(
        self,
        height: float = 0.5
    ) -> None:
        """Adds empty cell to PDF object.

        Args:
            height (float, optional): Height of empty cell. 
                Uses whatever format PDF uses, by default in inches. Defaults to 0.5.
        """
        self.pdf.multi_cell(w=0, h=height, border=0, ln=1)


    def set_cell_fill_color(
        self,
        r: int,
        g: int,
        b: int
    ) -> None:
        """Sets fill color for PDF object.

        Args:
            r (int): Red value (0-255)
            g (int): Green value (0-255)
            b (int): Blue value (0-255)
        """
        self.pdf.set_fill_color(r, g, b)


    def add_one_cell_row(
        self,
        text: str,
        align: str = "C",
        page_width: float = 8.5,
        margin: float = 0.5,
        border: Union[int, str] = 1,
        new_line: int = 1,
        fill: bool = False,
        cell_height: float = 0.5,
        r: int = 0,
        g: int = 0,
        b: int = 0
    ) -> None:
        """Add one cell row.

        Args:
            text (str): Text to add to cell.
            align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            page_width (float, optional): Width of page in given 
                format (default inches). Defaults to 8.5.
            margin (float, optional): Margin of page in given format 
                (default inches). Defaults to 0.5.
            border (Union[int, str], optional): Can be 0, 1, or string 
                containing LRTB (Left, Right, Top, Bottom) in any order. Defaults to 1.
            new_line (int, optional): Indicates if you want the final cell to require 
                subsequent cell to a new line. Options are 0 (no new line) 
                and 1 (new line). Defaults to 1.
            fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell_height (float, optional): Height of cell. 
                Uses whatever format PDF uses, by default in inches. Defaults to 0.5.
            r (int, optional): Color code for red (0-255). Defaults to 0.
            g (int, optional): Color code for green (0-255). Defaults to 0.
            b (int, optional): Color code for blue (0-255). Defaults to 0.
        """
        if fill:
            self.set_cell_fill_color(r, g, b)
        page_width: float = page_width - (margin * 2)

        self.pdf.set_xy(self.pdf.l_margin, self.pdf.y)
        self.pdf.cell(
            w=page_width,
            h=cell_height,
            txt=text,
            align=align,
            border=border,
            ln=new_line,
            fill=fill
        )


    def add_two_cell_row(
        self,
        cell1_text: str,
        cell2_text: str,
        cell1_align: str = "C",
        cell2_align: str = "C",
        page_width: float = 8.5,
        margin: float = 0.5,
        border: Union[int, str] = 1,
        new_line: int = 1,
        cell1_fill: bool = False,
        cell2_fill: bool = False,
        cell_height: float = 0.5,
        cell1_width: float = 0.5,
        cell2_width: float = 0.5,
        r: int = 0,
        g: int = 0,
        b: int = 0
    ) -> None:
        """Add two cell row.

        Args:
            cell1_text (str): Text to add to cell.
            cell2_text (str): Text to add to cell.
            cell1_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell2_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            page_width (float, optional): Width of page in given format (default inches). 
                Defaults to 8.5.
            margin (float, optional): Margin of page in given format 
                (default inches). Defaults to 0.5.
            border (Union[int, str], optional): Can be 0, 1, or string 
                containing LRTB (Left, Right, Top, Bottom) in any order. Defaults to 1.
            new_line (int, optional): Indicates if you want the final cell to require 
                subsequent cell to a new line. Options are 0 (no new line) and 
                1 (new line). Defaults to 1.
            cell1_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell2_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell_height (float, optional):Height of cell. 
                Uses whatever format PDF uses, by default in inches. Defaults to 0.5.
            cell1_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.5.
            cell2_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.5.
            r (int, optional): Color code for red (0-255). Defaults to 0.
            g (int, optional): Color code for green (0-255). Defaults to 0.
            b (int, optional): Color code for blue (0-255). Defaults to 0.

        Raises:
            ValueError: Given width percentages must add up to 1.
        """
        if cell1_fill or cell2_fill:
            self.set_cell_fill_color(r, g, b)

        if cell1_width + cell2_width != 1:
            raise ValueError(
                f"Cell widths must add up to 1. "
                f"Currently widths {cell1_width} and {cell2_width}"
                f"add up to ", cell1_width + cell2_width
                )

        page_width: float = page_width - (margin * 2)
        cell1_width: float = page_width * cell1_width
        cell2_width: float = page_width * cell2_width
        y_position: float = self.pdf.y

        self.pdf.set_xy(self.pdf.l_margin, y_position)
        self.pdf.multi_cell(
            w=cell1_width,
            h=cell_height,
            txt=cell1_text,
            align=cell1_align,
            border=border,
            fill=cell1_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width, y_position)
        self.pdf.multi_cell(
            w=cell2_width,
            h=cell_height,
            txt=cell2_text,
            align=cell2_align,
            border=border,
            ln=new_line,
            fill=cell2_fill
        )


    def add_three_cell_row(
        self,
        cell1_text: str,
        cell2_text: str,
        cell3_text: str,
        cell1_align: str = "C",
        cell2_align: str = "C",
        cell3_align: str = "C",
        page_width: float = 8.5,
        margin: float = 0.5,
        border: Union[int, str] = 1,
        new_line: int = 1,
        cell1_fill: bool = False,
        cell2_fill: bool = False,
        cell3_fill: bool = False,
        cell_height: float = 0.5,
        cell1_width: float = (1/3),
        cell2_width: float = (1/3),
        cell3_width: float= (1/3),
        r: int = 0,
        g: int = 0,
        b: int = 0
    ) -> None:
        """Add three cell row.

        Args:
            cell1_text (str): Text to add to cell.
            cell2_text (str): Text to add to cell.
            cell3_text (str): Text to add to cell.
            cell1_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell2_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell3_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            page_width (float, optional): Width of page in given format (default inches). 
                Defaults to 8.5.
            margin (float, optional): Margin of page in given format 
                (default inches). Defaults to 0.5.
            border (Union[int, str], optional): Can be 0, 1, or string 
                containing LRTB (Left, Right, Top, Bottom) in any order. Defaults to 1.
            new_line (int, optional): Indicates if you want the final cell to require 
                subsequent cell to a new line. Options are 0 (no new line) and 
                1 (new line). Defaults to 1.
            cell1_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell2_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell3_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell_height (float, optional):Height of cell. 
                Uses whatever format PDF uses, by default in inches. Defaults to 0.5.
            cell1_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.333.
            cell2_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.333.
            cell3_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.333.
            r (int, optional): Color code for red (0-255). Defaults to 0.
            g (int, optional): Color code for green (0-255). Defaults to 0.
            b (int, optional): Color code for blue (0-255). Defaults to 0.

        Raises:
            ValueError: Given width percentages must add up to 1.
        """
        if cell1_fill or cell2_fill or cell3_fill:
            self.set_cell_fill_color(r, g, b)

        if cell1_width + cell2_width + cell3_width != 1:
            raise ValueError(
                f"Cell widths must add up to 1. "
                f"Currently widths {cell1_width}, {cell2_width}, and {cell3_width} add up to ", 
                cell1_width + cell2_width + cell3_width
                )

        page_width: float = page_width - (margin * 2)
        cell1_width: float = page_width * cell1_width
        cell2_width: float = page_width * cell2_width
        cell3_width: float = page_width * cell3_width
        y_position: float = self.pdf.y

        self.pdf.set_xy(self.pdf.l_margin, y_position)
        self.pdf.multi_cell(
            w=cell1_width,
            h=cell_height,
            txt=cell1_text,
            align=cell1_align,
            border=border,
            ln=0,
            fill=cell1_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width, y_position)
        self.pdf.multi_cell(
            w=cell2_width,
            h=cell_height,
            txt=cell2_text,
            align=cell2_align,
            border=border,
            ln=0,
            fill=cell2_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width + cell2_width, y_position)
        self.pdf.multi_cell(
            w=cell3_width,
            h=cell_height,
            txt=cell3_text,
            align=cell3_align,
            border=border,
            ln=new_line,
            fill=cell3_fill
        )


    def add_four_cell_row(
        self,
        cell1_text: str,
        cell2_text: str,
        cell3_text: str,
        cell4_text: str,
        cell1_align: str = "C",
        cell2_align: str = "C",
        cell3_align: str = "C",
        cell4_align: str = "C",
        page_width: float = 8.5,
        margin: float = 0.5,
        border: Union[int, str] = 1,
        new_line: int = 1,
        cell1_fill: bool = False,
        cell2_fill: bool = False,
        cell3_fill: bool = False,
        cell4_fill: bool = False,
        cell_height: float = 0.5,
        cell1_width: float = 0.25,
        cell2_width: float = 0.25,
        cell3_width: float = 0.25,
        cell4_width: float = 0.25,
        r: int = 0,
        g: int = 0,
        b: int = 0
    ) -> None:
        """Add four cell row.

        Args:
            cell1_text (str): Text to add to cell.
            cell2_text (str): Text to add to cell.
            cell3_text (str): Text to add to cell.
            cell4_text (str): Text to add to cell.
            cell1_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell2_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell3_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell4_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            page_width (float, optional): Width of page in given format (default inches). 
                Defaults to 8.5.
            margin (float, optional): Margin of page in given format 
                (default inches). Defaults to 0.5.
            border (Union[int, str], optional): Can be 0, 1, or string 
                containing LRTB (Left, Right, Top, Bottom) in any order. Defaults to 1.
            new_line (int, optional): Indicates if you want the final cell to require 
                subsequent cell to a new line. Options are 0 (no new line) and 
                1 (new line). Defaults to 1.
            cell1_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell2_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell3_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell4_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell_height (float, optional):Height of cell. 
                Uses whatever format PDF uses, by default in inches. Defaults to 0.5.
            cell1_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.25.
            cell2_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.25.
            cell3_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.25.
            cell4_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.25.
            r (int, optional): Color code for red (0-255). Defaults to 0.
            g (int, optional): Color code for green (0-255). Defaults to 0.
            b (int, optional): Color code for blue (0-255). Defaults to 0.

        Raises:
            ValueError: Given width percentages must add up to 1.
        """
        if cell1_fill or cell2_fill or cell3_fill or cell4_fill:
            self.set_cell_fill_color(r, g, b)

        if cell1_width + cell2_width + cell3_width + cell4_width != 1:
            raise ValueError(
                f"Cell widths must add up to 1. "
                f"Currently widths {cell1_width}, {cell2_width}, {cell3_width}, and {cell4_width} "
                f"add up to ", cell1_width + cell2_width + cell3_width + cell4_width
                )

        page_width: float = page_width - (margin * 2)
        cell1_width: float = page_width * cell1_width
        cell2_width: float = page_width * cell2_width
        cell3_width: float = page_width * cell3_width
        cell4_width: float = page_width * cell4_width
        y_position: float = self.pdf.y

        self.pdf.set_xy(self.pdf.l_margin, y_position)
        self.pdf.multi_cell(
            w=cell1_width,
            h=cell_height,
            txt=cell1_text,
            align=cell1_align,
            border=border,
            ln=0,
            fill=cell1_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width, y_position)
        self.pdf.multi_cell(
            w=cell2_width,
            h=cell_height,
            txt=cell2_text,
            align=cell2_align,
            border=border,
            ln=0,
            fill=cell2_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width + cell2_width, y_position)
        self.pdf.multi_cell(
            w=cell3_width,
            h=cell_height,
            txt=cell3_text,
            align=cell3_align,
            border=border,
            ln=0,
            fill=cell3_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width +
                cell2_width + cell3_width, y_position)
        self.pdf.multi_cell(
            w=cell4_width,
            h=cell_height,
            txt=cell4_text,
            align=cell4_align,
            border=border,
            ln=new_line,
            fill=cell4_fill
        )


    def add_five_cell_row(
        self,
        cell1_text: str,
        cell2_text: str,
        cell3_text: str,
        cell4_text: str,
        cell5_text: str,
        cell1_align: str = "C",
        cell2_align: str = "C",
        cell3_align: str = "C",
        cell4_align: str = "C",
        cell5_align: str = "C",
        page_width: float = 8.5,
        margin: float = 0.5,
        border: Union[int, str] = 1,
        new_line: int = 1,
        cell1_fill: bool = False,
        cell2_fill: bool = False,
        cell3_fill: bool = False,
        cell4_fill: bool = False,
        cell5_fill: bool = False,
        cell_height: float = 0.5,
        cell1_width: float = 0.2,
        cell2_width: float = 0.2,
        cell3_width: float = 0.2,
        cell4_width: float = 0.2,
        cell5_width: float = 0.2,
        r: int = 0,
        g: int = 0,
        b: int = 0
    ) -> None:
        """Add five cell row.

        Args:
            cell1_text (str): Text to add to cell.
            cell2_text (str): Text to add to cell.
            cell3_text (str): Text to add to cell.
            cell4_text (str): Text to add to cell.
            cell5_text (str): Text to add to cell.
            cell1_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell2_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell3_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell4_align (str, optional): Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            cell5_align (str, optional):Set text alignment inside the cell. 
                Possible values are: 
                L : left align; 
                C: center; 
                X: center around current x position; 
                R: right align. 
                Defaults to "C".
            page_width (float, optional): Width of page in given format (default inches). 
                Defaults to 8.5.
            margin (float, optional): Margin of page in given format 
                (default inches). Defaults to 0.5.
            border (Union[int, str], optional): Can be 0, 1, or string 
                containing LRTB (Left, Right, Top, Bottom) in any order. Defaults to 1.
            new_line (int, optional): Indicates if you want the final cell to require 
                subsequent cell to a new line. Options are 0 (no new line) and 
                1 (new line). Defaults to 1.
            cell1_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell2_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell3_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell4_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell5_fill (bool, optional): Option to fill cell with set color. Defaults to False.
            cell_height (float, optional):Height of cell. 
                Uses whatever format PDF uses, by default in inches. Defaults to 0.5.
            cell1_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.2.
            cell2_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.2.
            cell3_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.2.
            cell4_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.2.
            cell5_width (float, optional): Width of cell as a percentage of 
                available space. Defaults to 0.2.
            r (int, optional): Color code for red (0-255). Defaults to 0.
            g (int, optional): Color code for green (0-255). Defaults to 0.
            b (int, optional): Color code for blue (0-255). Defaults to 0.

        Raises:
            ValueError: Given width percentages must add up to 1.
        """
        if cell1_fill or cell2_fill or cell3_fill or cell4_fill or cell5_fill:
            self.set_cell_fill_color(r, g, b)

        if cell1_width + cell2_width + cell3_width + cell4_width + cell5_width != 1:
            raise ValueError(
                f"Cell widths must add up to 1. "
                f"Currently widths {cell1_width}, {cell2_width}, {cell3_width}, {cell4_width} "
                f"and {cell5_width} add up to ", 
                cell1_width + cell2_width + cell3_width + cell4_width + cell5_width
                )

        page_width: float = page_width - (margin * 2)
        cell1_width: float = page_width * cell1_width
        cell2_width: float = page_width * cell2_width
        cell3_width: float = page_width * cell3_width
        cell4_width: float = page_width * cell4_width
        cell5_width: float = page_width * cell5_width
        y_position: float = self.pdf.y

        self.pdf.set_xy(self.pdf.l_margin, y_position)
        self.pdf.multi_cell(
            w=cell1_width,
            h=cell_height,
            txt=cell1_text,
            align=cell1_align,
            border=border,
            ln=0,
            fill=cell1_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width, y_position)
        self.pdf.multi_cell(
            w=cell2_width,
            h=cell_height,
            txt=cell2_text,
            align=cell2_align,
            border=border,
            ln=0,
            fill=cell2_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width + cell2_width, y_position)
        self.pdf.multi_cell(
            w=cell3_width,
            h=cell_height,
            txt=cell3_text,
            align=cell3_align,
            border=border,
            ln=0,
            fill=cell3_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width +
                cell2_width + cell3_width, y_position)
        self.pdf.multi_cell(
            w=cell4_width,
            h=cell_height,
            txt=cell4_text,
            align=cell4_align,
            border=border,
            ln=0,
            fill=cell4_fill
        )

        self.pdf.set_xy(self.pdf.l_margin + cell1_width + cell2_width +
                cell3_width + cell4_width, y_position)
        self.pdf.multi_cell(
            w=cell5_width,
            h=cell_height,
            txt=cell5_text,
            align=cell5_align,
            border=border,
            ln=new_line,
            fill=cell5_fill
        )


    def export(
        self,
        filename: str
    ) -> None:
        """Exports PDF object to file.

        Args:
            filename (str): Name of file to export to.
        """
        self.pdf.output(filename)
