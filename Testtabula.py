import tabula
import pandas as pd

# Read pdf into DataFrame
df = tabula.read_pdf("test.pdf", pages='all', multiple_tables=True)
#print(df[1].dropna(how='all'))
writer = pd.ExcelWriter('output.xlsx')
i = 0
for tab in df:
    i += 1
    tab = tab.iloc[3:,]
    tab.to_excel(writer, 'Sheet'+str(i))

writer.save()


