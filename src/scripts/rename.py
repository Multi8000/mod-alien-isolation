# ======================================================================================
# Projeto: Alien: Isolation - Aprimoramentos
# Autor: Marcos Martins
# Data: 10/2020
# Github: https://github.com/multi8000
# LinkedIn: https://www.linkedin.com/in/marcos-martins0
# ======================================================================================


# ======================================================================================
# Bibliotecas
# ======================================================================================
import os, subprocess, re


# ======================================================================================
# Variáveis locais
# ======================================================================================


# ======================================================================================
# Ações
# ======================================================================================

nome_arquivo = "/desktop/mod-alien-isolation/original/ui/dump.txt"

with open(nome_arquivo, 'r') as arquivo:

    for linha in arquivo:

        if "File" in linha:
            
            linha_tab = linha.split(' ')
            print(linha_tab[1])


"""
# Renomeia os arquivos (defasado)
for root4, directory4, files4 in os.walk(dir_destino):
    for file4 in files4:
        file_name4, file_extension4 = os.path.splitext(file4)

        if file4.endswith(".merged"):
            For_search = file_name4[-8:-4]

            #nome_arquivo_modificado = re.findall(r'\d+', nome_arquivo_modificado)
            #nome_arquivo_modificado = nome_arquivo_modificado[0]
            #print(nome_arquivo_modificado)


        for root2, directory2, files2 in os.walk(dir_arquivos_wem_originais):
            for file2 in files2:
                file_name2, file_extension2 = os.path.splitext(file2)

                if file2.endswith(".wem") and For_search in file2:
                    Original_file = file2

                    Old_name = f"{dir_destino}/{file4}"
                    New_name = f"{dir_destino}/{Original_file}"

                    os.rename(Old_name, New_name)
"""