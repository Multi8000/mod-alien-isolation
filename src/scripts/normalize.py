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
import os, subprocess, sys, re, librosa, pathlib


# ======================================================================================
# Variáveis locais
# ======================================================================================
dir_home = pathlib.Path.home()
dir_arquivos_origem = f"{dir_home}/desktop/mod-alien-isolation/processos/normalizar_wav/para_normalizar"
dir_arquivos_destino = f"{dir_home}/desktop/mod-alien-isolation/processos/normalizar_wav/normalizado"


# ======================================================================================
# Funções
# ======================================================================================
def procura_palavra_dentro_do_arquivo(nome_arquivo, palavra_para_procurar):

    numero_linha = 0
    lista_de_resultados = []
    regex = re.compile(r"[\d\+|\-|.|]")

    with open(nome_arquivo, 'r') as arquivo:

        for linha in arquivo:

            numero_linha += 1

            if palavra_para_procurar in linha:

                if "Parsed_volumedetect" in str(linha):
                    linha = str(linha)
                    linha = linha.replace("']", "")
                    posicao_cortar_texto = linha.find("]")
                    comprimento_texto = len(linha)
                    linha = linha[posicao_cortar_texto+2:comprimento_texto]
                    lista_de_resultados.append((linha.rstrip()))
                else:
                    lista_de_resultados.append((linha.rstrip()))

    resultado = regex.findall(str(lista_de_resultados))
    resultado = ''.join(resultado)
    resultado = float(resultado)

    return resultado


# ======================================================================================
# Ações
# ======================================================================================

# Normaliza o volume do arquivo .WAV
for (raiz, subdiretorios, arquivos) in os.walk(dir_arquivos_origem):

    for arquivo in arquivos:

        nome_arquivo, extensao = os.path.splitext(arquivo)

        # Verifica se o arquivo .WAV tem um comprimento maior ou igual a 3 segundos, pois o algoritmo 'lournorm', que é baseado na métrica LUFS, tem por premissa que o arquivo deva ter 3 segundos ou mais de comprimento
        if(librosa.get_duration(filename = f'{dir_arquivos_origem}/{nome_arquivo}.wav')) >= 3:

            # Mede as estatísticas do arquivo .WAV e exporta para um arquivo .TXT
            script = f'ffmpeg -y -hide_banner -nostdin -i "{dir_arquivos_origem}/{nome_arquivo}.wav" -af loudnorm=I=-16:dual_mono=true:TP=-1.5:lra=11:print_format=summary -f null -y nul 2> "{dir_arquivos_origem}/estatisticas_{nome_arquivo}.txt"'
            subprocess.call(script, shell = True)


            # Lê o arquivo de estatisticas, captura os valores e armazena em variáveis
            arquivo_estatisticas = f"{dir_arquivos_origem}/estatisticas_{nome_arquivo}.txt"

            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Integrated") == 0:
                integrated_input = -24
            else:
                integrated_input = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Integrated")


            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input True Peak") == 0:
                true_peak = -2
            else:
                true_peak = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input True Peak")


            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input LRA") == 0:
                lra = 7
            else:
                lra = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input LRA")


            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Threshold") == 0:
                threshold = -25
            else:
                threshold = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Threshold")

            
            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Target Offset") == 0:
                target_offset = 0
            else:
                target_offset = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Target Offset")


            # Corrige o volume do arquivo baseado nas estatísticas que foram exportadas
            script = f'ffmpeg -y -i "{dir_arquivos_origem}/{nome_arquivo}.wav" -af loudnorm=I=-16:TP=-1.5:lra=11.0:measured_I={integrated_input}:measured_TP={true_peak}:lra={lra}:measured_thresh={threshold}:offset={target_offset}:linear=true:print_format=summary "{dir_arquivos_destino}/{nome_arquivo}.wav"'
            subprocess.call(script, shell = True)


        # Se o comprimento do arquivo for menor do que 3 segundos, então... 
        else:

            # Preenche o arquivo .WAV com 'null audio' até que ele atinja 3 segundos
            comprimento_audio = librosa.get_duration(filename = f'{dir_arquivos_origem}/{nome_arquivo}.wav')
            incremento_necessario = (3 - comprimento_audio)

            script = f'ffmpeg -y -f lavfi -t {incremento_necessario} -i anullsrc=channel_layout=stereo:sample_rate=44100 -i "{dir_arquivos_origem}/{nome_arquivo}.wav" -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1" "{dir_arquivos_origem}/{nome_arquivo}_incrementado.wav"'
            subprocess.call(script, shell = True)


            # Mede as estatísticas do arquivo .WAV e exporta para um arquivo .TXT
            script = f'ffmpeg -y -hide_banner -nostdin -i "{dir_arquivos_origem}/{nome_arquivo}_incrementado.wav" -af loudnorm=I=-16:dual_mono=true:TP=-1.5:lra=11:print_format=summary -f null -y nul 2> "{dir_arquivos_origem}/estatisticas_{nome_arquivo}.txt"'
            subprocess.call(script, shell = True)


            # Lê o arquivo de estatisticas, captura os valores e armazena em variáveis
            arquivo_estatisticas = f"{dir_arquivos_origem}/estatisticas_{nome_arquivo}.txt"

            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Integrated") == 0:
                integrated_input = -24
            else:
                integrated_input = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Integrated")


            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input True Peak") == 0:
                true_peak = -2
            else:
                true_peak = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input True Peak")


            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input LRA") == 0:
                lra = 7
            else:
                lra = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input LRA")


            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Threshold") == 0:
                threshold = -25
            else:
                threshold = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Input Threshold")

            
            if procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Target Offset") == 0:
                target_offset = 0
            else:
                target_offset = procura_palavra_dentro_do_arquivo(arquivo_estatisticas, "Target Offset")


            # Corrige o volume do arquivo baseado nas estatísticas que foram exportadas
            script = f'ffmpeg -y -i "{dir_arquivos_origem}/{nome_arquivo}_incrementado.wav" -af loudnorm=I=-16:TP=-1.5:lra=11.0:measured_I={integrated_input}:measured_TP={true_peak}:lra={lra}:measured_thresh={threshold}:offset={target_offset}:linear=true:print_format=summary "{dir_arquivos_destino}/{nome_arquivo}_normalizado.wav"'
            subprocess.call(script, shell = True)


            # Corta o arquivo .wav excluindo o 'null audio', mantendo seu comprimento original
            script = f'ffmpeg -y -i "{dir_arquivos_destino}/{nome_arquivo}_normalizado.wav" -af atrim={incremento_necessario}:3 "{dir_arquivos_destino}/{nome_arquivo}.wav"'
            subprocess.call(script, shell = True)


        # Deleta os arquivos .WAV auxiliares que foram criados ao longo do processo
        os.remove(f"{dir_arquivos_origem}/{nome_arquivo}_incrementado.wav")
        os.remove(f"{dir_arquivos_destino}/{nome_arquivo}_normalizado.wav")