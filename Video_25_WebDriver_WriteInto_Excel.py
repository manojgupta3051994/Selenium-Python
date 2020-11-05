import openpyxl

path = "C:/Users/Manoj/Desktop/Python - Selenium Practice/Drivers/WriteIntoExcel.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active

for i in range(1,6):
    for j in range(1,4):
        sheet.cell(row=i,column=j).value='Manoj'


workbook.save(path)