import csv
import numpy as np
import pandas as pd
import plotly_express as px

def getData(path, column1, column2):
    col1=[]
    col2=[]
    with open(path) as f:
      data=csv.DictReader(f)
      for row in data:
          col1.append(float(row[column1]))
          col2.append(float(row[column2]))
    return{"x": col1, "y": col2}
    
def findCorrelation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("The correlation for your data set is", correlation[0,1], ".")
    num=correlation[0,1]
    if num > 0:
      print("It is a positive number, which means your data is related in some way.")
    elif num == 0:
     print("It is zero, so your data isn't related at all.")
    else:
      print("It is a negative number, so it is related inversely.")


def main():
    print("Data Analyzation and Graph Program")
    path = input("Enter the path of the file that you would like to analyze.")
    line1 = pd.read_csv(path)
    
    if(path):
        with open(path, "r") as file:
            first_line = file.readline()
        print("Here are the choices for x and y:", first_line)
        print("Copy and paste these into the sections below.")
        column1 = input("Enter the column name for x.")
        column2 = input("Enter the column name for y.")
        data= getData(path, column1, column2)
        findCorrelation(data)
        yes= input("Would you like to graph this data?")
        if(yes=="yes"):
            new= input("Which type of graph would you like? Scatter, Line, or bar? Please type in lowercase.")
            if(new=="line"):
                print("Opening line graph...")
                graph =px.line(line1, x=column1, y=column2)
                graph.show()
                print("Line graph opened.")
            elif(new=="scatter"):
                print("Opening scatter graph...")
                graph =px.scatter(line1, x=column1, y=column2)
                graph.show()
                print("Scatter graph opened.")
            elif(new=="bar"):
                print("Opening bar graph...")
                graph =px.bar(line1, x=column1, y=column2)
                graph.show()
                print("Bar graph opened.")
            elif(new != "bar" or "scatter" or "line"):
                print("That was not a valid option....")
        else:
            print("Okay. Exiting program...")
main()
 