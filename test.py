from pdf_helper import *

# Create New PDF
new_pdf = create_pdf()

# Add Page
add_page(new_pdf)

# Add 1 Cell Row - Align Center
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Center")

# Add 2 Cell Row - Align Center
add_two_cell_row(
    new_pdf,
    cell1_text="Add 2 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 2 Cell Row - Cell 2 - Align Center",
)

# Add 3 Cell Row - Align Center
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Center",
)

# Add 4 Cell Row - Align Center
add_four_cell_row(
    new_pdf,
    cell1_text="Add 4 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 4 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 4 Cell Row - Cell 3 - Align Center",
    cell4_text="Add 4 Cell Row - Cell 4 - Align Center",
)

# Add 5 Cell Row - Align Center

# Add 1 Cell Row - Align Left
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Left", align="L")

# Add 2 Cell Row - Align Left
add_two_cell_row(
    new_pdf,
    cell1_text="Add 2 Cell Row - Cell 1 - Align Left",
    cell2_text="Add 2 Cell Row - Cell 2 - Align Left",
    cell1_align="L",
    cell2_align="L"
)

# Add 3 Cell Row - Align Left
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Left",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Left",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Left",
    cell1_align="L",
    cell2_align="L",
    cell3_align="L"
)

# Add 4 Cell Row - Align Left
add_four_cell_row(
    new_pdf,
    cell1_text="Add 4 Cell Row - Cell 1 - Align Left",
    cell2_text="Add 4 Cell Row - Cell 2 - Align Left",
    cell3_text="Add 4 Cell Row - Cell 3 - Align Left",
    cell4_text="Add 4 Cell Row - Cell 4 - Align Left",
    cell1_align="L",
    cell2_align="L",
    cell3_align="L",
    cell4_align="L"
)

# Add 5 Cell Row - Align Left

# Add 1 Cell Row - Align Right
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Right", align="R")


# Add 2 Cell Row - Align Right
add_two_cell_row(
    new_pdf,
    cell1_text="Add 2 Cell Row - Cell 1 - Align Right",
    cell2_text="Add 2 Cell Row - Cell 2 - Align Right",
    cell1_align="R",
    cell2_align="R"
)

# Add 3 Cell Row - Align Right
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Right",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Right",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Right",
    cell1_align="R",
    cell2_align="R",
    cell3_align="R"
)

# Add 4 Cell Row - Align Right
add_four_cell_row(
    new_pdf,
    cell1_text="Add 4 Cell Row - Cell 1 - Align Right",
    cell2_text="Add 4 Cell Row - Cell 2 - Align Right",
    cell3_text="Add 4 Cell Row - Cell 3 - Align Right",
    cell4_text="Add 4 Cell Row - Cell 4 - Align Right",
    cell1_align="R",
    cell2_align="R",
    cell3_align="R",
    cell4_align="R"
)

# Add 5 Cell Row - Align Right

# Add Empty Row

# Change Fill Color

# Change Font

# Added 2 new pages
add_page(new_pdf)
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Center",
)

add_page(new_pdf)
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Center",
)

# Export PDF
export_pdf(new_pdf, "test.pdf")
