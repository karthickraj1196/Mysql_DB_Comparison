#########file Compraison
import mysql.connector
import xlrd
import pandas as pd



qadb = mysql.connector.connect(host='host1',user='user',password='password',port='port1')
uatdb = mysql.connector.connect(host='host2',user='root',password='password',port='port2')
sql = "Your_Query"

qadf = pd.read_sql(sql,qadb)
uatdf = pd.read_sql(sql,uatdb)

qadf.to_excel('QAipt.xls',index=False)
uatdf.to_excel('UATipt.xls',index=False)

qadata = pd.read_excel('QAipt.xls')
uatdata = pd.read_excel('UATipt.xls')

qapd = pd.DataFrame(qadata)
uatpd = pd.DataFrame(uatdata)
#outpd = pd.DataFrame(columns = ['File_Path'])

flag = 0
i = 0

#for row in uatpd.iterrows():
#   j = 0
#   for row in qapd.iterrows():
#      if uatpd.loc[i,'RULEFILE_LOCATION'] == qapd.loc[j,'RULEFILE_LOCATION']:
#          print(i,j, "Same")
#          print(qapd.loc[i,'RULEFILE_LOCATION'])
#          print(uatpd.loc[j,'RULEFILE_LOCATION'])
#           flag = 0
#      else:
#          print(i,j, "NotSame")
#          print(uatpd.loc[i,'RULEFILE_LOCATION'])
#          outpd.append({'File_Path' : uatpd.loc[i,'RULEFILE_LOCATION']},{'File_Status' : uatpd.loc[i,'ACTIVE']})
#          flag = 1
#      j = j + 1
#   if flag == 1:
#      print(uatpd.loc[i,'RULEFILE_LOCATION'])
#      outpd.append({'File_Path' : uatpd.loc[i,'RULEFILE_LOCATION']},{'File_Status' : uatpd.loc[i,'ACTIVE']}) 
#   i = i + 1

print("QA----------UAT")
#i = 0
#for row in qapd.iterrows():
#   j = 0
#   for row in uatpd.iterrows():
#      if qapd.loc[i,'RULEFILE_LOCATION'] == uatpd.loc[j,'RULEFILE_LOCATION']:
#           flag = 0
#      else:
#           flag = 1
#   j = j +1
#   if flag == 1:
#      print(uatpd.loc[i,'RULEFILE_LOCATION'])
#   i = i + 1
#outpd.to_excel('Result.xls')
#outpd['File_Path'].where(qapd.values['RULEFILE_LOCATION']==uatpd.values['RULEFILE_LOCATION'])


#output = uatpd[~uatpd.RULEFILE_LOCATION.isin(qapd.RULEFILE_LOCATION.values)]
#output1 = uatpd[~uatpd.ACTIVE.isin(qapd.ACTIVE.values)]
#print(output)
#print(output1)


output = {'UAT_DIFF':uatpd, 'QA_DIFF':qapd}
outputpd = pd.concat(output)
outputpd1 = outputpd.drop_duplicates(keep=False)
#outputpd1.to_excel('Result.xls',index=True)
print(outputpd1.to_string())
