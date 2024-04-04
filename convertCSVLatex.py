# desenvolvido por:RAFAEL DOS SANTOS FERREIRA
# 


import csv
import glob
import pandas as pd


def csv_to_latex(csv_file_path, latex_file_path):
    latex_code = []
    
    # Inicializa o código LaTeX
    latex_code.append(r"\begin{table}[htb]")
    latex_code.append(r"\footnotesize")
    latex_code.append(r"\captionsetup{justification=centering}")    
    latex_code.append(r"\center")
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        # Processa o cabeçalho para determinar o número de colunas
        header = next(csv_reader)
        num_columns = len([cell for cell in header if cell.strip()])
        latex_code.append(r"\begin{tabular}{" + "r" * num_columns + "}")
        latex_code.append(r"\hline")
        
        # Processa o cabeçalho
        latex_code.append(r"\rowcolor[HTML]{EFEFEF} ")
        latex_code.append(" & ".join([f"\\multicolumn{{1}}{{c}}{{\\cellcolor[HTML]{{EFEFEF}}\\textbf{{{cell.strip()}}}}}" for cell in header if cell.strip()]) + r" \\ \hline")
        
        # Processa as linhas restantes
        for i, row in enumerate(csv_reader):
            if i % 2 == 1:
                latex_code.append(" & ".join([cell.strip() for cell in row if cell.strip()]) + r" \\")
            else:
                latex_code.append(r"\cellcolor[HTML]{EFEFEF} " + " & \cellcolor[HTML]{EFEFEF}".join([cell.strip() for cell in row]) + r" \\ ")                    
        
    
    # Finaliza o código LaTeX
    latex_code.append(r"\hline")
    latex_code.append(r"\end{tabular}")
    latex_code.append(r"\caption{Resultados do modulo Corte}")
    latex_code.append(r"\label{tbCorte}")
    latex_code.append(r"\end{table}")
    
    # Salva o código LaTeX em um arquivo
    with open(latex_file_path, 'w') as latex_file:
        latex_file.write("\n".join(latex_code))

    with open(latex_file_path, 'r') as file:
        latex_document = file.read()
        file.close()    

    latex_document =  latex_document.replace('AppS_1','$AppS_{1}$')
    latex_document =  latex_document.replace('AppS_2','$AppS_{2}$')
    latex_document =  latex_document.replace('AppS_3','$AppS_{3}$')
    latex_document =  latex_document.replace('AppS_4','$AppS_{4}$')


    latex_document =  latex_document.replace('AppS1','$AppS_{1}$')
    latex_document =  latex_document.replace('AppS2','$AppS_{2}$')
    latex_document =  latex_document.replace('AppS3','$AppS_{3}$')
    latex_document =  latex_document.replace('AppS4','$AppS_{4}$')


    latex_document =  latex_document.replace('AppS 1','$AppS_{1}$')
    latex_document =  latex_document.replace('AppS 2','$AppS_{2}$')
    latex_document =  latex_document.replace('AppS 3','$AppS_{3}$')
    latex_document =  latex_document.replace('AppS 4','$AppS_{4}$')


    latex_document =  latex_document.replace('AXCS11','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS12','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS13','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS14','$AXCS1_{4}$')

    latex_document =  latex_document.replace('AXCS21','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS22','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS23','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS24','$AXCS1_{4}$')

    latex_document =  latex_document.replace('AXCS31','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS32','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS33','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS34','$AXCS1_{4}$')


    latex_document =  latex_document.replace('AXCS41','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS42','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS43','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS44','$AXCS1_{4}$')






    latex_document =  latex_document.replace('AXCS1_1','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS1_2','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS1_3','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS1_4','$AXCS1_{4}$')


    latex_document =  latex_document.replace('AXCS2_1','$AXCS2_{1}$')
    latex_document =  latex_document.replace('AXCS2_2','$AXCS2_{2}$')
    latex_document =  latex_document.replace('AXCS2_3','$AXCS2_{3}$')
    latex_document =  latex_document.replace('AXCS2_4','$AXCS2_{4}$')

    latex_document =  latex_document.replace('AXCS3_1','$AXCS3_{1}$')
    latex_document =  latex_document.replace('AXCS3_2','$AXCS3_{2}$')
    latex_document =  latex_document.replace('AXCS3_3','$AXCS3_{3}$')
    latex_document =  latex_document.replace('AXCS3_4','$AXCS3_{4}$')

    latex_document =  latex_document.replace('AXCS4_1','$AXCS4_{1}$')
    latex_document =  latex_document.replace('AXCS4_2','$AXCS4_{2}$')
    latex_document =  latex_document.replace('AXCS4_3','$AXCS4_{3}$')
    latex_document =  latex_document.replace('AXCS4_4','$AXCS4_{4}$')
    latex_document =  latex_document.replace('%','\%')
    with open(latex_file_path, 'w') as file:
        file.write(latex_document)    



pasta_csv = '/run/media/rsf/vms/python/csv/blocosFixo/*.csv'  # O asterisco (*) e usado como curinga para buscar todos os arquivos CSV

# Use glob.glob para encontrar todos os arquivos que correspondem ao padrao
arquivos_csv = glob.glob(pasta_csv)
print(arquivos_csv)

# Itere sobre a lista de arquivos CSV encontrados
for csv_file_path in arquivos_csv:
    csv_to_latex(csv_file_path,csv_file_path.replace('.csv', '.tex') )


print("concluido")
