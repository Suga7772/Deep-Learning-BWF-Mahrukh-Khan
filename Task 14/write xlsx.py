import xlsxwriter

# Workbook() takes one, non-optional, argument which is the filename that we want to create.
workbook = xlsxwriter.Workbook('examples/ex3.xlsx')

# The workbook object is then used to add new worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# using worksheet obj to write data via write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')

# Finally, close the Excel file
workbook.close()