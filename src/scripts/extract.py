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
import os, subprocess, pathlib


# ======================================================================================
# Variáveis locais
# ======================================================================================
dir_home = pathlib.Path.home()
dir_arquivos_origem = f"{dir_home}/desktop/mod-alien-isolation/original"
dir_arquivos_destino = f"{dir_home}/desktop/mod-alien-isolation/processos/extrair_pck_bnk"
dir_rscanner_console = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/ravioligametools/rscannerconsole.exe"


# ======================================================================================
# Ações
# ======================================================================================

# Extrai o conteúdo original dos arquivos .BNK ou .PCK e gera uma lista com os nomes no formato que o jogo reconhece
for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_origem):

    # Nome da pasta atual que estamos navegando, para que posteriormente seja criado no diretório de destino uma pasta com este mesmo nome para colocar os arquivos extraídos
    nome_pasta_atual = os.path.basename(raiz)

    for arquivo in arquivos:

        # Se as pastas não existirem, então cria no diretório destino para serem colocados os arquivos extraídos
        if not os.path.exists(f"{dir_arquivos_destino}/{nome_pasta_atual}"):
            os.mkdir(f"{dir_arquivos_destino}/{nome_pasta_atual}")

        # Extrai os arquivos .WEM e .DAT do arquivo .BNK ou .PCK
        script = f"{dir_rscanner_console} {raiz}/{arquivo} /extract:{dir_arquivos_destino}/{nome_pasta_atual} /unknowns"
        subprocess.call(script, shell = True)

        # Gera uma lista com todos os arquivos extraídos e seus nomes originais
        script = f"{dir_rscanner_console} {raiz}/{arquivo} /list > {dir_arquivos_destino}/{arquivo}.txt"
        subprocess.call(script, shell = True)