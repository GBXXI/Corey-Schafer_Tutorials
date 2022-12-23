
"""Refractoring G.Bitsonis"""
# https://altoconvertpdftoexcel.com/ kai smallpdf (prosoxh poiasthlh (h g na einai nomizw))
import os
import sys
from datetime import datetime
from calendar import monthrange

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from openpyxl import Workbook, load_workbook

plt.close('all')


def asking_date():
    """ Asking the user for the desired date with the current date as default,
        returning a set with: a tuple with the weeknumber and the monthnumber, the month and the wear.
    """

    user_input = input(
        f"The current date is: {datetime.now().strftime('%m-%Y')}, \n"
        "Do you want another date? (Y/N) "
    )

# CAUTION, an infinate loop may arise, if the user does not pass an acceptable answer!
    if user_input.lower().strip() == "y" or user_input.lower().strip() == "yes":

              user_input_year = int(input("Enter the year: "))
              user_input_month = int(input("Enter the month: "))

              try:
                     days_of_month = monthrange(user_input_year, user_input_month)

              except Exception as e:
                     days_of_month = asking_date()

              return (days_of_month, user_input_month, user_input_year)

    elif user_input.lower().strip() == "n" or user_input.lower().strip() == "no":

              days_of_month = monthrange(datetime.now().year, datetime.now().month)
              return (days_of_month, datetime.now().month, datetime.now().year)
    else:
              print("Not a valid response!")
              days_of_month = asking_date()


def main():

       file_directory = os.getcwd()

       if sys.platform.startswith('win32'):
              report = f"\\\\?\{file_directory}\\test_report_{datetime.now().strftime('%d-%m-%Y-%H:%M:%S')}.xlsx"  # Managing long path name for  windows.
       else:
              report = f"{file_directory}/test_report_{datetime.now().strftime('%d-%m-%Y-%H:%M:%S')}.xlsx"

       # Opening a workbook for our report and assigning our active sheet.
       # template_wb = load_workbook('a_test.xlsx')
       # ws = template_wb.active

       date = asking_date()
       month_days = date[0][1]  # Accessing the 2nd element of our tuple.

       report_lines = [7, 10, 11, 14, 15, 22, 23, 33, 37, 49]


       for day in range (1, month_days+1):

              # Creating 0 values dataframe for the days that no reports are present.
              if not os.path.exists(f"{file_directory}{os.sep}{day}.xlsx"):
                     print(f"No report for day: {day}, exists")
                     df_values = pd.Series(0, index = report_lines)

                     df_values.iloc[[0]] = datetime.fromisoformat(

                            f'{date[2]}-{f"{str(date[1])}".zfill(2)}-{str(day).zfill(2)}'

                     ).strftime('%d-%M-%Y') # Passing our date value.
              else:
                     print(f"Report for day: {day}")
                     #read our data from excel
                     df_data = pd.read_excel(f'{day}.xlsx')

                     df_values = df_data.iloc[
                            [value for value in report_lines],
                            5
                     ]

                     df_values.iloc[[0]] = df_data.iloc[7, 3].strftime('%d-%M-%Y')  # Passing our date value.

       print(df_values)

       # #to x apeikonizei th mera (dld th seira) sto excel anaforas
       # for x in range(4,month_days+4):
       #        #for x in megethi:
       #        #pernaw tis wres leitourgias twn gennhtriwn
       #        #epilegw to keli sto opoio tha eisagw timh
       #        wcell=ws.cell(x,2)
       #        #eisagw timh apo ton "pinaka"
       #        wcell.value=pinakas.loc[10,y]
       #        wcell=ws.cell(x,3)
       #        wcell.value=pinakas.loc[11,y]
       #        #pernaw tis mwh
       #        wcell=ws.cell(x,6)
       #        wcell.value=pinakas.loc[14,y]/1000
       #        wcell=ws.cell(x,7)
       #        wcell.value=pinakas.loc[15,y]/1000
       #        #pernaw tis mvarh
       #        wcell=ws.cell(x,9)
       #        wcell.value=pinakas.loc[22,y]/1000
       #        wcell=ws.cell(x,10)
       #        wcell.value=pinakas.loc[23,y]/1000
       #        #pernaw nm3 kai mj aeriou
       #        wcell=ws.cell(x,23)
       #        wcell.value=pinakas.loc[37,y]
       #        wcell=ws.cell(x,24)
       #        wcell.value=pinakas.loc[33,y]
       #        #pernaw thermal energy
       #        wcell=ws.cell(x,36)
       #        wcell.value=pinakas.loc[49,y]
       #        y=y+1


       # Saving our report.
       # template_wb.save(report)

              ###pinakas.plot();
              #ypologismoi=pd.Dataframe()
              #ypologismoi=pinakas
              #del ypologismoi[k]
              #maxValues = ypologismoi.max(axis = 1)
              #minValues = ypologismoi.min(axis=1)
              #minValues=pd.concat([minValues,maxValues], axis=1)
              #minValues.columns = ["min","max"]
              #minValues.index=["h1","h2","p1","p2","q1","q2","mj","nm3","scv"]
              #print(minValues)
       return None


if __name__ == '__main__':
       main()
