import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Marks In Percentage"]))
            sleep.append(float(row["Days Present"]))

    return {"x": coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks vs Days Present: - \n------>", correlation[0,1])

def setup():
    data_path = "StudentsMarksvsDaysPresent.csv"

    datasource = getDataSource(data_path)

    findCorrelation(datasource)
    plotFigure(data_path)
