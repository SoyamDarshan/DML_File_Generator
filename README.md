# DML_File_Generator

# What the code the code does?

It takes an excel file which has the table name, field names, datatypes, maximum length, precision length, Nullable etc.
The code takes the excel file and prepares a DML file.


## Using the xlrd module for conduction operations in Excel files.


```
import xlrd
```


The name of the excel file with the details.

```
wb = xlrd.open_workbook('structures.xls')
```

Assigning values to the numeric and string datatypes as all these varieties fall under the same catagory

```
numbers = ['numeric', 'smallint', 'bigint', 'tinyint', 'int', 'decimal']
str = ['varchar', 'char', 'string', 'nvarchar', 'nchar']
```

## NOTE : Can use dictionary instead of list for faster search time




All the cells accessed, have a specific content and the format of the cells is always same in all Excel sheet provided.


```
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
```

