import tkinter as tk
from tkinter import filedialog, messagebox
from cleanData import clean_data
from loadData import load_csv
from graphs import salaryDistributionHistogram, summaryStatsTable
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class JobMarketAnalyzerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Job Market Analyzer")
        self.root.geometry("1000x1000")
        self.root.configure(bg = "white")
        self.df = None

        self.label = tk.Label(root, text="Job Market Analysis Tool", font =("Arial", 20, "bold"), bg = "white", fg = "black")
        self.label.pack(pady=20)

        buttonsStyle = {"bg": "#0056b3", "fg": "black", "font":("Arial", 10, "bold"), "width": 25, "pady": 10}
        self.uploadButton = tk.Button(root, text = "Upload CSV", command = self.loadFile, **buttonsStyle)
        self.uploadButton.pack(pady=10)

        self.statusLabel = tk.Label(root, text = "No data loaded", bg = "white", fg = "red")
        self.statusLabel.pack()

        self.buttonFrame = tk.Frame(root, bg = "white")
        self.buttonFrame.pack(pady=20)

        self.statsButton = tk.Button(self.buttonFrame, text="View Summary Statistics", state="disabled", command=self.showStats,  **buttonsStyle)
        self.statsButton.grid(row = 0, column = 0, padx = 10)

        self.distibutionButton = tk.Button(self.buttonFrame, text="View Salary Distribution", state="disabled", command=self.showDistribution,  **buttonsStyle)
        self.distibutionButton.grid(row = 0, column = 1, padx = 10)

        self.chartFrame = tk.Frame(root, bg = "white")
        self.chartFrame.pack(fill = "both", expand = True, pady = 20, padx = 20 )


    def loadFile(self):
        filePath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filePath:
            try:
                rawData = load_csv(filePath)
                self.df = clean_data(rawData)

                self.statusLabel.config(text = f"Loaded: {filePath.split('/')[-1]}")
                self.statsButton.config(state = "normal")
                self.distibutionButton.config(state = "normal")
                messagebox.showinfo("Success", "File processed succesfully.")
            except Exception as e:
                messagebox.showerror("Error:", str(e))

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