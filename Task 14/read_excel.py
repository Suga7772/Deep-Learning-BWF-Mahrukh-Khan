import pandas as pd
import openpyxl

xlsx = pd.ExcelFile('examples/ex1.xlsx')
print(pd.read_excel(xlsx, 'Sheet1'))

# we can also pass file path to to_excell to avoid excel_writer

writer = pd.ExcelWriter('examples/ex2.xlsx')
xlsx.to_excel(writer, 'Sheet1')
writer.save()

# xlsx.to_excel('example/ex2.xlsx')  avoid line 9,10 with one line script
