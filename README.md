# Job Market Analyzer

## AI Assistance Statement

This README file was created with AI assistance to provide a simple reference while coding this project. The content and information was sourced from our original project proposal (planned features, team responsibilities, and file structure). AI was used only to organize and format the information clearly.

### Ayati
- Core logic:
  - Data cleaning and validation
  - Skill frequency analyzer
  - Jobs by location and industry
- User Interface
- Testing / Validation
- Documentation

### Victoria
- Core logic:
  - CSV file upload
  - Data cleaning
  - Salary distribution chart
  - Summary statistics
- User Interface
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

### Jobs by Location & Industry
Displays job counts grouped by location and industry.

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