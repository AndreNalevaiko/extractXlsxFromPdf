import re, os
import pandas as pd
from tabula import read_pdf

pdf_files = []
for root, dirs, files in os.walk("."):
    for filename in files:
        regex_pdf = re.compile("^.*\.pdf")

        if regex_pdf.match(filename):
            pdf_files.append(filename)

for pdf_file in pdf_files:
    dfs = read_pdf(pdf_file, pages='all', multiple_tables=True)

    dfs_elegibles = []

    for df in dfs:
        if len(df.columns) > 3:
            dfs_elegibles.append(df)

    df_concatenated = pd.concat(dfs_elegibles)
    df_concatenated.replace(r'\\n',' ', regex=True)

    folder_name = pdf_file + ' planilha'
    
    try:
        os.mkdir(folder_name)
    except:
        pass

    df_concatenated.to_excel('{}/planilha.xlsx'.format(folder_name), index=False, header=False)

    # import ipdb; ipdb.set_trace()
print('teste')
