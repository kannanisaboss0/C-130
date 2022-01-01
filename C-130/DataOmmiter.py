#--------------------------------------------DataOmmiter.py--------------------------------------------#

'''
Importing Modules:
-pandas (pd)
-csv
'''

import pandas as pd 
import csv


#Reading data from the dataset and creating binary model of it on the basis of null and not-null
df=pd.read_csv("Merged.csv")
df_bin=df.notnull()

#Defining the ,ist of columns in the dataset
columns_list=["Mass","Distance","Radius"]

#Defining a function to remove rows form the dataset that contain undefined values
def DeleteRowsAccordingtoColumn(column):

  #Running a for loop over the range of zero to the length of the dataset column minus one
  for index,ele in enumerate(df[column]):

    #Verifying whether each value of the binary model of the dataset column is ture or not
    #Case-1~ the value is not true - it is removed 
    if df_bin[column][index]!=True:
      df.drop([index],inplace=True)

#Running a for loop over the columns list and adding each element as an argument to a function
for column in columns_list:
  DeleteRowsAccordingtoColumn(column)

#Creating an input for the user to enter a file name of their discretion
file_name=input("Please enter the file name:")

#Verifying if the file name has "." in it or not
#Case-1~ "." is present - "." is removed by splitting the name
if "." in file_name:
  file_title,file_ext=file_name.split(".")
  file_name=file_title

#Creating a file with the name given by the user
with open(file_name+".csv","w") as fl:

  #Initiating a writer and writing data from the refined dataet into a new file
  writer=csv.writer(fl)
  writer.writerow(["Name","Distance","Mass","Radius"])

  #Running a for loop over the range of zero to the length of the dataset column minus one
  for iteration in range(len(df)-1):

    #Using a try block, to avoid any index errors
    #Try
    try:
      writer.writerow([df["Name"][iteration],df["Mass"][iteration],df["Radius"][iteration],df["Distance"][iteration]])

    #Except  
    except:
      None  

#Printing the thank you message
print("Thank you for using DataOmmiter.py") 

#--------------------------------------------DataOmmiter.py--------------------------------------------#