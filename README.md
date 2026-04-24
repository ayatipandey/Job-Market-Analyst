# Job Market Analyzer

## AI Assistance Statement

This README file was created with AI assistance to provide a simple reference while coding this project. The content and information was sourced from our original project proposal (planned features, team responsibilities, and file structure). AI was used only to organize and format the information clearly.

### Ayati
- Core logic:
  - CSV File uplaod
  - Data cleaning and validation
- User Interface
- Testing / Validation
- Documentation

### Victoria
- Core logic:
  - Jobs by Skills chart
  - Jobs by Work Type chart
  - Salary distribution chart
  - Summary statistics table
- Testing / Validation
- Documentation

---

## Features

### CSV File Upload
Allows the user to browse and select a CSV file from their computer.

### Data Cleaning & Validation
Checks for missing values, invalid entries, and prepares the dataset for analysis.

### Skill Frequency Analyzer
Parses the job description column and counts common skills or keywords.

### Salary Distribution Chart
Calculates and displays:
- Mean salary
- Median salary
- Minimum salary
- Maximum salary

### Jobs by Location & Work Type
Displays job counts grouped by work type.

### Summary Statistics
Shows key figures in a structured table inside the GUI.

---

## File Structure

main.py         # Main file to run the program
gui.py          # Tkinter graphical user interface
loadData.py     # Reads CSV files using pandas
cleanData.py    # Cleans and validates data
analyzeData.py  # Calculates stats and frequencies
graphs.py       # Builds charts, graphs, and tables
README.md       # Project documentation