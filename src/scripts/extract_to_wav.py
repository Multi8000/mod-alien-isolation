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
import os, subprocess, shutil, pathlib


# ======================================================================================
# Variáveis locais
# ======================================================================================
dir_home = pathlib.Path.home()
dir_arquivos_origem = f"{dir_home}/desktop/mod-alien-isolation/original"
dir_arquivos_destino = f"{dir_home}/desktop/mod-alien-isolation/processos/extrair_pck_bnk_para_wav"
dir_quickbms = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/quickbms.exe"
dir_quickbms_script = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/wavescan.bms"
dir_bnkextr = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/bnkextr.exe"
dir_ww2ogg = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/ww2ogg.exe"
dir_ww2ogg_script = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/packed_codebooks_aotuv_603.bin"
dir_revorb = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/revorb.exe"
dir_ffmpeg = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwiseunpacker/ffmpeg.exe"


# ======================================================================================
# Ações
# ======================================================================================

# Extrai o arquivo bruto .WAV (ainda inaudível)
for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_origem):
    
    # Nome da pasta atual que estamos navegando, para que posteriormente seja criado no diretório de destino uma pasta com este mesmo nome para colocar os arquivos extraídos
    nome_pasta_atual = os.path.basename(raiz)
    dir_atual = os.getcwd()

    for arquivo in arquivos:

        # Se as pastas não existirem, então cria no diretório destino para serem colocados os arquivos extraídos
        if not os.path.exists(f"{dir_arquivos_destino}/{nome_pasta_atual}"):
            os.mkdir(f"{dir_arquivos_destino}/{nome_pasta_atual}")

        # Extrai os arquivos com formato .PCK
        if arquivo.endswith(".PCK"):
            script = f"{dir_quickbms} {dir_quickbms_script} {raiz}/{arquivo} {dir_arquivos_destino}/{nome_pasta_atual}"
            subprocess.call(script)

        # Extrai os arquivos com formato .BNK
        if arquivo.endswith(".BNK"):
            script = f"{dir_bnkextr} {raiz}/{arquivo}"
            subprocess.call(script)

            # Move os arquivos do diretório atual para a pasta no diretório de destino criada no começo do script
            for arquivo in os.listdir(dir_atual):
                if arquivo.endswith(".wav"):

                    de = f"{dir_atual}/{arquivo}"
                    para = f"{dir_arquivos_destino}/{nome_pasta_atual}/{arquivo}"
                    shutil.move(de, para)



# Monta o arquivo .wav e converte para um .ogg (sem perda de qualidade)
for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_destino):

    for arquivo in arquivos:
        if arquivo.endswith(".wav"):
            script = f"{dir_ww2ogg} {raiz}/{arquivo} --pcb {dir_ww2ogg_script}"
            subprocess.call(script)

            if arquivo.endswith(".wav"):
                os.remove(f"{raiz}/{arquivo}")

    # Revorb do arquivo .WAV
    for arquivo in arquivos:
        if arquivo.endswith(".wav"):
            script = f"{dir_revorb} {raiz}/{arquivo}"
            subprocess.call(script) # deixar comentado e testar fazer o mod sem passar pelo processo de revorb, poupando uma etapa desse longo processo



# Faz a conversão de .ogg para .wav, pois é o formato original extraído do jogo
for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_destino):
    
    for arquivo in arquivos:
        if arquivo.endswith(".ogg"):
            script = f"{dir_ffmpeg} -hide_banner -nostdin -i {raiz}/{arquivo} -acodec pcm_s16le -ar 44100 -y {raiz}/{arquivo}.wav"
            subprocess.call(script)

            if arquivo.endswith(".ogg"):
                os.remove(f"{raiz}/{arquivo}")