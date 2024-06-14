import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_bar_graph(df):
    df.plot(kind='bar')
    plt.title('Bar Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def create_line_graph(df):
    df.plot(kind='line')
    plt.title('Line Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def create_pie_chart(df):
    plt.figure(figsize=(8, 8))
    df.iloc[:, 0].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

def create_3d_graph(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], c='r', marker='o')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.title('3D Graph')
    plt.show()

def create_box_plot(df):
    df.boxplot()
    plt.title('Box Plot')
    plt.show()

def create_histogram(df):
    df.hist()
    plt.suptitle('Histogram')
    plt.show()
