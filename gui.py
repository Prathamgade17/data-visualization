import tkinter as tk
from tkinter import filedialog
import pandas as pd
import logic

def upload_excel():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            display_table(df)
        except Exception as e:
            print("Error:", e)

def display_table(df):
    top = tk.Toplevel(root)
    top.title("Excel Data")
    table = logic.Table(top, dataframe=df, showtoolbar=True, showstatusbar=True)
    table.show()

def create_bar_graph():
    if 'df' in globals():
        logic.create_bar_graph(df)
    else:
        print("No data loaded. Please upload an Excel file.")

def create_line_graph():
    if 'df' in globals():
        logic.create_line_graph(df)
    else:
        print("No data loaded. Please upload an Excel file.")

def create_pie_chart():
    if 'df' in globals():
        logic.create_pie_chart(df)
    else:
        print("No data loaded. Please upload an Excel file.")

def create_3d_graph():
    if 'df' in globals():
        logic.create_3d_graph(df)
    else:
        print("No data loaded. Please upload an Excel file.")

def create_box_plot():
    if 'df' in globals():
        logic.create_box_plot(df)
    else:
        print("No data loaded. Please upload an Excel file.")

def create_histogram():
    if 'df' in globals():
        logic.create_histogram(df)
    else:
        print("No data loaded. Please upload an Excel file.")

root = tk.Tk()
root.title("Excel File Analyzer")

upload_button = tk.Button(root, text="Upload Excel File", command=upload_excel)
upload_button.pack(pady=10)

bar_button = tk.Button(root, text="Bar Graph", command=create_bar_graph)
bar_button.pack(pady=5)

line_button = tk.Button(root, text="Line Graph", command=create_line_graph)
line_button.pack(pady=5)

pie_button = tk.Button(root, text="Pie Chart", command=create_pie_chart)
pie_button.pack(pady=5)

graph3d_button = tk.Button(root, text="3D Graph", command=create_3d_graph)
graph3d_button.pack(pady=5)

box_button = tk.Button(root, text="Box Plot", command=create_box_plot)
box_button.pack(pady=5)

histogram_button = tk.Button(root, text="Histogram", command=create_histogram)
histogram_button.pack(pady=5)

root.mainloop()
