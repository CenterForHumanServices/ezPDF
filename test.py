from pdf_helper import *

# Create New PDF
new_pdf = create_pdf()

# Add Page
add_page(new_pdf)

# Add 1 Cell Row - Align Center
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Center")

# Add 2 Cell Row - Align Center

# Add 3 Cell Row - Align Center

# Add 4 Cell Row - Align Center

# Add 5 Cell Row - Align Center

# Add 1 Cell Row - Align Left
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Left", align="L")

# Add 2 Cell Row - Align Left

# Add 3 Cell Row - Align Left

# Add 4 Cell Row - Align Left

# Add 5 Cell Row - Align Left

# Add 1 Cell Row - Align Right
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Right", align="R")


# Add 2 Cell Row - Align Right

# Add 3 Cell Row - Align Right

# Add 4 Cell Row - Align Right

# Add 5 Cell Row - Align Right

# Add Empty Row

# Change Fill Color

# Change Font

# Export PDF
export_pdf(new_pdf, "test.pdf")
