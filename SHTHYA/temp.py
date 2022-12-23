# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

 

import pandas as pd
from openpyxl import *


#orizw excel kai sheet sta opoia tha apothikeysw (exel anaforas mhna)
wb=load_workbook('a.xlsx')
ws=wb['b']

#ftiaxnw series gia na exw ta onomata twn excel pou tha anoiksw
dates=pd.Series(['1.xlsx','2.xlsx','3.xlsx','4.xlsx','5.xlsx','6.xlsx',
                 '7.xlsx','8.xlsx','9.xlsx','10.xlsx'])

#zhtaw inputs gia na treksei to programma toses meres kai gia na mhn exv thema me thn kenh mera
n=int(input("poses meres exei o mhnas?  "))
k=int(input("poia mera den exoume metrhsh?  "))


#loupa gia na ginoun read ola ta excel apo ta opoia antlw dedomena ( pltithos report = mere mhna)
for m in range (0,n):
#otan ftasw sth mera pou den exei report kane skip (PREPEI NA TO ALLASW NA KANEI MHDEN)
        if m==k-1:
            print("den exeis metrhsh")
            pass
        else :
#diabase to exel ths kathe meras
            print(dates[m])
            dfa=pd.read_excel(dates[m])
#pare thn pempth sthlh apo to excel ths meras
            dfb=dfa.iloc[:,5]
#pare ta soixeia poy me endiaferoun apo th sthh
            df1=dfb[[x for x in [0,1,3,4,9,10,16,21]]]
            #an einai h prwth epanalhpsh dhmiourgw thn prwth sthlh
            if m==0:
                dedomena=pd.DataFrame(df1)
#stis epomenes epanalhpseis prosthetw sthles
            else:
                dedomena.merge(df1, left_on='lkey', right_on='rkey')
                
      

            

