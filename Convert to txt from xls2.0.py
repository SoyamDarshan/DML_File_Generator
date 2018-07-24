import xlrd
wb = xlrd.open_workbook('closedaccounts_cancellationsaudit.xls') #name of xls file
sheet = wb.sheet_by_index(1) #sheet number starting from 0
data=""
numbers=['numeric','smallint','bigint','tinyint','int','decimal']
strin=['varchar','char','String','nvarchar','nchar']
data1="\n"
f1=open('new_text_dml.txt','w') #output text file
f1.write("record")
f1.write(data1)
for i in range(sheet.nrows):
    if((sheet.cell(i,1).value) in strin):
        data="utf8 string(\"\x01\", maximum_length=" + str((sheet.cell(i,2).value)) + ") " + (sheet.cell(i,0).value).lower() + " =" + (sheet.cell(i,4).value).upper() + ";"
        print (data)
        f1.write(data)
        f1.write(data1)
    elif(sheet.cell(i,1).value in numbers):
        if((sheet.cell(i,3).value)):
            data="decimal(\",\"." + str((sheet.cell(i,3).value)) + ", maximum_length="+str((sheet.cell(i,2).value))+") "+(sheet.cell(i,0).value).lower()  +" =" + (sheet.cell(i,4).value).upper()+";"
        else:
            data="decimal(\",\"," + str((sheet.cell(i,3).value)) + ", maximum_length="+str((sheet.cell(i,2).value))+") "+(sheet.cell(i,0).value).lower()  +" =" + (sheet.cell(i,4).value).upper()+";"
        print (data)
        f1.write(data)
        f1.write(data1)
    elif(sheet.cell(i,1).value == 'date'):
        data="date(\"yyyy-mm-dd\")(\",\") "+(sheet.cell(i,0).value).lower()  +" =" + (sheet.cell(i,4).value).upper()+";"
        print (data)
        f1.write(data)
        f1.write(data1)
    elif(sheet.cell(i,1).value == 'bit'):
        data="decimal(\",\",0, maximum_length=1) "+(sheet.cell(i,0).value).lower()  +" =" + (sheet.cell(i,4).value).upper()+";"
        print (data)
        f1.write(data)
        f1.write(data1)
    elif(sheet.cell(i,1).value == 'datetime' or sheet.cell(i,1).value == 'datetime2'):
        data="datetime(\"yyyy-mm-dd HH24:MI:SS.NN\")(\",\") "+(sheet.cell(i,0).value).lower()  +" =" + (sheet.cell(i,4).value).upper()+";"
        print (data)
        f1.write(data)
        f1.write(data1)
f1.write("end")        
f1.close()
#hierarchyid , datetime2 , address not there need format for dml
