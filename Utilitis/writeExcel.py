import openpyxl

workbook = openpyxl.load_workbook("/Volumes/Entertainme/Automation/goibiboNewProject/Excel/testdata.xlsx")
sheet = workbook["Login.test"]

sheet.cell(row=4, column=3).value="age"
workbook.save("/Volumes/Entertainme/Automation/goibiboNewProject/Excel/testdata.xlsx")