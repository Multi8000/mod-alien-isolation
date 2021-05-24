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
dir_arquivos_origem = f"{dir_home}/desktop/mod-alien-isolation/processos/normalizar_wav/normalizado"
dir_arquivos_destino = f"{dir_home}/desktop/mod-alien-isolation/processos/converter_wav_para_wem"
dir_wwise_command_line = "c:/program files (x86)/audiokinetic/wwise 2019.2.6.7381/authoring/x64/release/bin/wwisecli.exe"
dir_wwise_xml = f"{dir_home}/desktop/mod-alien-isolation/processos/normalizar_wav/arquivos.wsources"
dir_wwise_projeto = f"{dir_home}/desktop/mod-alien-isolation/ferramentas/wwise/mod-alien-isolation/mod-alien-isolation.wproj"


# ======================================================================================
# Ações
# ======================================================================================

# Gera o arquivo .XML com as origens e destinos, que será lido pelo Wwise e convertido de .WAV para .WEM, assim, possibilitando juntarmos todos os arquivos .WEM e empacotar em um arquivo .PCK ou .BNK

if os.path.exists(dir_wwise_xml):
    os.remove(dir_wwise_xml)

with open(dir_wwise_xml, "w") as gera_arquivo_xml:
    gera_arquivo_xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    gera_arquivo_xml.write(f"<ExternalSourcesList SchemaVersion=\"1\" Root=\"{dir_arquivos_origem}\">\n")

    for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_origem):
        for arquivo in arquivos:

            gera_arquivo_xml.write(f"\t<Source Path=\"{arquivo}\" Conversion=\"Vorbis Quality High\" />\n")

    gera_arquivo_xml.write("</ExternalSourcesList>")


# Converte os arquivos de origem que estão contidos no .XML para .WEM
script = f"\"{dir_wwise_command_line}\" \"{dir_wwise_projeto}\" -ConvertExternalSources \"{dir_wwise_xml}\" -ExternalSourcesOutput \"{dir_arquivos_destino}\""
subprocess.call(script)