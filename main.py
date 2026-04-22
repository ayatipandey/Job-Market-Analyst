import tkinter as tk
from gui import JobMarketAnalyzerApp


if __name__ == "__main__":
    # Initalise Tkinter 
    root = tk.Tk()
    # Instantiate the JobMarketAnalyzerApp
    app = JobMarketAnalyzerApp(root)
    root.mainloop()

