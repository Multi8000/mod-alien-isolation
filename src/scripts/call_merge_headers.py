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
import os, subprocess, shutil, re, pathlib


# ======================================================================================
# Variáveis locais
# ======================================================================================
dir_home = pathlib.Path.home()
dir_arquivos_wem_originais = f"{dir_home}/desktop/mod-alien-isolation/processos/extrair_pck_bnk" # terão várias pastas, precisa acessar com um FOR
dir_arquivos_wem_modificados = f"{dir_home}/desktop/mod-alien-isolation/processos/converter_wav_para_wem" # terão várias pastas?
dir_destino = f"{dir_home}/desktop/mod-alien-isolation/processos/mesclar_cabecalho_wem"
dir_avisos = f"{dir_home}/desktop/mod-alien-isolation/processos/avisos"
dir_python_26 = f"{dir_home}/appdata/local/programs/python/python26/python.exe"
dir_script_mesclar_cabecalho_wem = f"{dir_home}/desktop/mod-alien-isolation/scripts/scripts-de-terceiros/compare_wem.py"


# ======================================================================================
# Ações
# ======================================================================================

# Arquivos modificados
for (raiz_arquivo_modificados, subdiretorios_arquivo_modificados, arquivos_modificados) in os.walk(dir_arquivos_wem_modificados):
    for arquivo_modificado in arquivos_modificados:

        nome_arquivo_modificado, extensao_arquivo_modificado = os.path.splitext(arquivo_modificado)
        
        nome_arquivo_modificado_offset = re.findall(r'\d+', nome_arquivo_modificado)
        nome_arquivo_modificado_offset = str(nome_arquivo_modificado_offset)
        nome_arquivo_modificado_offset = nome_arquivo_modificado_offset.replace("['", "")
        nome_arquivo_modificado_offset = nome_arquivo_modificado_offset.replace("']", "")
        nome_arquivo_modificado_offset = '0000' + nome_arquivo_modificado_offset
        nome_arquivo_modificado_offset = nome_arquivo_modificado_offset[-4:]
        

        if arquivo_modificado.endswith(".wem"):

            # Arquivos originais
            for (raiz_arquivo_originais, subdiretorios_arquivo_originais, arquivos_originais) in os.walk(dir_arquivos_wem_originais):
                for arquivo_original in arquivos_originais:

                    nome_arquivo_original, extensao_arquivo_original = os.path.splitext(arquivo_original)
                    
                    nome_arquivo_original_offset = re.findall(r'\d+', nome_arquivo_original)
                    nome_arquivo_original_offset = str(nome_arquivo_original_offset)
                    nome_arquivo_original_offset = nome_arquivo_original_offset.replace("['", "")
                    nome_arquivo_original_offset = nome_arquivo_original_offset.replace("']", "")


                    if arquivo_original.endswith(".wem") and nome_arquivo_modificado_offset in nome_arquivo_original_offset:

                        # Verificar se o arquivo modificado é maior que o arquivo original, se sim, escreve no arquivo de log
                        tamanho_arquivo_original = os.stat(f"{raiz_arquivo_originais}/{arquivo_original}").st_size
                        tamanho_arquivo_modificado = os.stat(f"{raiz_arquivo_modificados}/{arquivo_modificado}").st_size

                        if tamanho_arquivo_original < tamanho_arquivo_modificado:
                            
                            with open(f"{dir_avisos}/Avisos_etapa_mesclar.txt", "a") as arquivo_avisos:

                                mensagem = f"ERRO: ARQUIVO MODIFICADO ({arquivo_modificado}) É MAIOR DO QUE O ARQUIVO ORIGINAL({arquivo_original}). Tamanho arquivo modificado: {tamanho_arquivo_modificado} bytes, tamanho arquivo original: {tamanho_arquivo_original} bytes.\n\n"
                                arquivo_avisos.write(mensagem)

                        else:

                            script = f"{dir_python_26} {dir_script_mesclar_cabecalho_wem} {raiz_arquivo_originais}/{arquivo_original} {raiz_arquivo_modificados}/{arquivo_modificado}"
                            subprocess.call(script)


# Move os arquivos .WEM
for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_wem_modificados):
    for arquivo in arquivos:
        
        if arquivo.endswith(".merged"):

            de = f"{raiz}/{arquivo}"
            para = f"{dir_destino}/{arquivo}"
            shutil.move(de, para)