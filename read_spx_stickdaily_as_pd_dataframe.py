from datetime import timedelta
import pandas as pd
from pandas.core.frame import Axis
from datetime import datetime
import gspread as gs

gc = gs.service_account(filename='service_account.json') 
sh=gc.open_by_url("https://docs.google.com/spreadsheets/d/1v2GbZla5N4fd6vo3JurotX0-XBkRruAm2CDLM4friLE") 
ws = sh.worksheet('Sheet1')
data = pd.DataFrame(ws.get_all_records())[['Date','Close']]          
data1=[]
for idx,row in data.iterrows():
    datecol=row['Date']
    row['Date']=datetime.strptime(datecol,"%Y-%m-%d")
    data1.append(row)
data=pd.DataFrame(data1)
data.head()
print(data)
