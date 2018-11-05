import tabula
import pandas as pd

# Read pdf into DataFrame
df = tabula.read_pdf("test.pdf", pages='all', multiple_tables=True)
#print(df[1].dropna(how='all'))


df = [df[i].iloc[3:,] for i in range(len(df))]

writer = pd.ExcelWriter('merge.xlsx', )
merge = pd.concat([i for i in df],ignore_index=True)
merge.to_excel(writer, 'merge')
writer.save()




#writer = pd.ExcelWriter('output.xlsx')
# i = 0
# for tab in df:
#     i += 1
#     tab = tab.iloc[3:,]
#     tab.to_excel(writer, 'Sheet'+str(i))

#writer.save()


