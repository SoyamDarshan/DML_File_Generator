import xlrd
wb = xlrd.open_workbook('structures.xls')
f1 = open('dml_name.txt','w')
sheet = wb.sheet_by_index(0)
data = ""
numbers = ['numeric', 'smallint', 'bigint', 'tinyint', 'int', 'decimal']
str = ['varchar', 'char', 'string', 'nvarchar', 'nchar']

for i in range(sheet.nrows):
    if sheet.cell(i,1).value in str:
        data = "utf8 string(\",\", maximum_length = "+sheet.cell(i,2).value+") "+(sheet.cell(i,0).value).lower() +"  = " + (sheet.cell(i,4).value).upper()+";\n"
        print (data)
        f1.write(data)
    elif sheet.cell(i,1).value in numbers :
        if sheet.cell(i,4).value == 0 or sheet.cell(i,4).value == '0' :
            data = "decimal(\",\"," + sheet.cell(i,3).value + ", maximum_length = "+sheet.cell(i,2).value+") "+(sheet.cell(i,0).value).lower()  +" = " + (sheet.cell(i,4).value).upper()+";\n"
        else:
            data="decimal(\",\"." + sheet.cell(i,3).value + ", maximum_length="+sheet.cell(i,2).value+") "+(sheet.cell(i,0).value).lower()  +" = " + (sheet.cell(i,4).value).upper()+";\n"
        print (data)
        f1.write(data)    
    elif sheet.cell(i,1).value == 'date' :
        data = "date(\"yyyy-mm-dd\")(\",\") "+(sheet.cell(i,0).value).lower()  +" = " + (sheet.cell(i,4).value).upper()+";\n"
        print (data)
        f1.write(data)    
    elif sheet.cell(i,1).value == 'bit' :
        data = "decimal(\",\",0, maximum_length = 1) "+(sheet.cell(i,0).value).lower()  +" = " + (sheet.cell(i,4).value).upper()+";\n"
        print (data)
        f1.write(data)   
    elif sheet.cell(i,1).value == 'datetime' or sheet.cell(i,1).value == 'datetime2':
        data = "datetime(\"yyyy-mm-dd HH24:MI:SS:NN,\")(\",\") "+(sheet.cell(i,0).value).lower()  +" = " + (sheet.cell(i,4).value).upper()+";\n"
        print (data)
        f1.write(data)
        
f1.close()
# hierarchyid , datetime2 , address not there need format for dml
