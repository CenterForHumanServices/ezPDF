from pdf_helper import *

# Create New PDF
print("Creating New PDF")
new_pdf = create_pdf()

# Add Page
print("Adding Page")
add_page(new_pdf)

# Add 1 Cell Row - Align Center
print("Adding 1 Cell Row - Align Center")
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Center")

# Add 2 Cell Row - Align Center
print("Adding 2 Cell Row - Align Center")
add_two_cell_row(
    new_pdf,
    cell1_text="Add 2 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 2 Cell Row - Cell 2 - Align Center",
)

# Add 3 Cell Row - Align Center
print("Adding 3 Cell Row - Align Center")
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Center",
)

# Add 4 Cell Row - Align Center
print("Adding 4 Cell Row - Align Center")
add_four_cell_row(
    new_pdf,
    cell1_text="Add 4 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 4 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 4 Cell Row - Cell 3 - Align Center",
    cell4_text="Add 4 Cell Row - Cell 4 - Align Center",
)

# Add 5 Cell Row - Align Center
print("Adding 5 Cell Row - Align Center")
add_five_cell_row(
    new_pdf,
    cell1_text="Add 5 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 5 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 5 Cell Row - Cell 3 - Align Center",
    cell4_text="Add 5 Cell Row - Cell 4 - Align Center",
    cell5_text="Add 5 Cell Row - Cell 5 - Align Center",
)

# Add 1 Cell Row - Align Left
print("Adding 1 Cell Row - Align Left")
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Left", align="L")

# Add 2 Cell Row - Align Left
print("Adding 2 Cell Row - Align Left")
add_two_cell_row(
    new_pdf,
    cell1_text="Add 2 Cell Row - Cell 1 - Align Left",
    cell2_text="Add 2 Cell Row - Cell 2 - Align Left",
    cell1_align="L",
    cell2_align="L"
)

# Add 3 Cell Row - Align Left
print("Adding 3 Cell Row - Align Left")
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
print("Adding 4 Cell Row - Align Left")
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
print("Adding 5 Cell Row - Align Center")
add_five_cell_row(
    new_pdf,
    cell1_text="Add 5 Cell Row - Cell 1 - Align Left",
    cell2_text="Add 5 Cell Row - Cell 2 - Align Left",
    cell3_text="Add 5 Cell Row - Cell 3 - Align Left",
    cell4_text="Add 5 Cell Row - Cell 4 - Align Left",
    cell5_text="Add 5 Cell Row - Cell 5 - Align Left",
    cell1_align="L",
    cell2_align="L",
    cell3_align="L",
    cell4_align="L",
    cell5_align="L"
)

# Add 1 Cell Row - Align Right
print("Adding 1 Cell Row - Align Right")
add_one_cell_row(new_pdf, "Add 1 Cell Row - Align Right", align="R")


# Add 2 Cell Row - Align Right
print("Adding 2 Cell Row - Align Right")
add_two_cell_row(
    new_pdf,
    cell1_text="Add 2 Cell Row - Cell 1 - Align Right",
    cell2_text="Add 2 Cell Row - Cell 2 - Align Right",
    cell1_align="R",
    cell2_align="R"
)

# Add 3 Cell Row - Align Right
print("Adding 3 Cell Row - Align Right")
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
print("Adding 4 Cell Row - Align Right")
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
print("Adding 5 Cell Row - Align Center")
add_five_cell_row(
    new_pdf,
    cell1_text="Add 5 Cell Row - Cell 1 - Align Right",
    cell2_text="Add 5 Cell Row - Cell 2 - Align Right",
    cell3_text="Add 5 Cell Row - Cell 3 - Align Right",
    cell4_text="Add 5 Cell Row - Cell 4 - Align Right",
    cell5_text="Add 5 Cell Row - Cell 5 - Align Right",
    cell1_align="R",
    cell2_align="R",
    cell3_align="R",
    cell4_align="R",
    cell5_align="R"
)

# Add Empty Row
print("Adding empty row")
add_empty_row(new_pdf)

# Creating row without border
print("Creating row without border")
add_one_cell_row(new_pdf, "Creating row without border", border=0)

# Create row without border and with fill
print("Creating row without border and with fill")
add_one_cell_row(
    new_pdf,
    "Creating row without border and with fill",
    border=0,
    fill=1,
    r=195,
    g=223,
    b=236)

# Create 3 row with border, and first cell is filled
print("Creating 3 row with border, and first cell is filled")
add_three_cell_row(
    new_pdf,
    cell1_text="Creating 3 row with border, and first cell is filled",
    cell2_text="Creating 3 row with border, and first cell is filled",
    cell3_text="Creating 3 row with border, and first cell is filled",
    cell1_fill=1,
    r=195,
    g=223,
    b=236,
)

# Attempt to overfill page
print("Attempting to overfill page by adding 10 rows")
for i in range(1, 11):
    add_one_cell_row(new_pdf, f"Add 1 Cell Row - Align Center - Row {i}")

# Change Fill Color

# Change Font

# Added 2 new pages
print("Adding new page")
add_page(new_pdf)

print("Adding 3 Cell Row - Align Center")
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Center",
)

print("Adding new page")
add_page(new_pdf)

print("Adding 3 Cell Row - Align Center")
add_three_cell_row(
    new_pdf,
    cell1_text="Add 3 Cell Row - Cell 1 - Align Center",
    cell2_text="Add 3 Cell Row - Cell 2 - Align Center",
    cell3_text="Add 3 Cell Row - Cell 3 - Align Center",
)

# Export PDF
print("Exporting PDF")
export_pdf(new_pdf, "example.pdf")
