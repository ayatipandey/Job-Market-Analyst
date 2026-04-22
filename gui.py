import tkinter as tk
from tkinter import filedialog, messagebox
from cleanData import clean_data
from loadData import load_csv
from graphs import salaryDistributionHistogram, summaryStatsTable, skillFrequencyBarChart, jobByWorkTypeBarChart
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class JobMarketAnalyzerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Job Market Analyzer")
        self.root.geometry("1100x900")
        self.root.configure(bg = "white")
        self.df = None

        # Header 
        self.header = tk.Frame (root, bg = "#003366", height = 120)
        self.header.pack(fill = "x", side = "top")
        self.headerLabel = tk.Label(self.header, text="Job Market Analysis Tool", font =("Arial", 25), bg = "#003366", fg = "white")
        self.headerLabel.pack(pady=20)

        # Control Panel
        self.controlFrame = tk.Frame (root, bg = "white", relief = "groove", bd = 1)
        self.controlFrame.pack(fill = "x", padx = 40, pady = 20)

        # Button style
        buttonsStyle = {"bg": "#003366", "fg": "white", "font":("Arial", 10, "bold"), "width": 25, "pady": 10}
        self.uploadButton = tk.Button(root, text = "Upload CSV", command = self.loadFile, **buttonsStyle)
        self.uploadButton.pack(pady=10)

        # File Status
        self.statusLabel = tk.Label(root, text = "No data loaded", bg = "white", fg = "red")
        self.statusLabel.pack()

        # Button grid
        self.buttonFrame = tk.Frame(root, bg = "white")
        self.buttonFrame.pack(pady=20)

        self.statsButton = tk.Button(self.buttonFrame, text="View Summary Statistics", state="disabled", command=self.showStats,  **buttonsStyle)
        self.statsButton.grid(row = 0, column = 0, padx = 10)

        self.distibutionButton = tk.Button(self.buttonFrame, text="View Salary Distribution", state="disabled", command=self.showDistribution,  **buttonsStyle)
        self.distibutionButton.grid(row = 0, column = 1, padx = 10)

        self.workTypeButton = tk.Button(self.buttonFrame, text="Jobs by Work Type", state="disabled", command=self.showWorkType,  **buttonsStyle)
        self.workTypeButton.grid(row = 1, column = 0, padx = 10)

        self.skillsButton = tk.Button(self.buttonFrame, text="Skills Frequency", state="disabled", command=self.showSkills,  **buttonsStyle)
        self.skillsButton.grid(row = 1, column = 1, padx = 10)

        # Main Content
        self.contentArea = tk.Frame (root, bg = "white")
        self.contentArea.pack(fill = "both",expand = True, padx = 40, pady = 10)
        self.chartFrame = tk.Frame(self.contentArea, bg = "white")
        self.chartFrame.pack(anchor = "center")

        # Footer
        self.footer = tk.Frame(root, bg = "#003366", height = 50 )
        self.footer.pack(fill = "x", side = "bottom")
        self.footerLabel = tk.Label(self.footer, text = "Job Market Analyzer | Introduction to Python Project by Ayati Pandey & Victoria Torres", font =("Arial", 12), bg = "#003366", fg = "white")
        self.footerLabel.pack(side = "right", padx = 20)
    
    # Loads CSV file
    def loadFile(self):
        filePath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filePath:
            try:
                rawData = load_csv(filePath)
                self.df = clean_data(rawData)

                self.statusLabel.config(text = f"Loaded: {filePath.split('/')[-1]}")
                self.statsButton.config(state = "normal")
                self.distibutionButton.config(state = "normal")
                self.workTypeButton.config(state = "normal") 
                self.skillsButton.config(state = "normal")
                messagebox.showinfo("Success", "File processed succesfully.")
            except Exception as e:
                messagebox.showerror("Error:", str(e))

    # Graphs 
    def embedFigures (self,fig):
        for widget in self.chartFrame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg (fig, master = self.chartFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill = "both", expand = True)

    def showStats(self):
        if self.df is not None:
            fig = summaryStatsTable(self.df)
            self.embedFigures(fig)
    
    def showDistribution(self):
        if self.df is not None:
            fig = salaryDistributionHistogram(self.df)
            self.embedFigures(fig)

    def showWorkType(self):
        if self.df is not None:
            fig = jobByWorkTypeBarChart(self.df)
            self.embedFigures(fig)

    def showSkills(self):
        if self.df is not None:
            plt.close('all')
            fig = skillFrequencyBarChart(self.df)
            self.embedFigures(fig)

    