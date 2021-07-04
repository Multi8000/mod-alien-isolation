"""
STEP 02

This script will convert the .WEM files
(extracted with __extract__ script) to .WAV files.

"""

from subprocess import (run, PIPE, DEVNULL)
from pathlib import Path

from __utils__ import make_directory


class Convert():

    def __init__(self):
        self.ww2ogg_path = 'src/tools/WwiseUnpacker/ww2ogg.exe'
        self.ww2ogg_codebooks_path = 'src/tools/WwiseUnpacker/packed_codebooks_aoTuV_603.bin'
        self.revorb_path = 'src/tools/WwiseUnpacker/revorb.exe'
        #self.input_path = ''
        #self.output_path = ''


    def convert_to_ogg(self, input_path: str) -> None:
        # Get the folder name from input_path and create the output_path
        # Example: 'src/temp/extracted/UI' turns 'src/temp/converted/UI'
        output_path = f'src/temp/converted/{Path(input_path).stem}'

        files_list = [file for file in Path(input_path).glob('*') if file.is_file()]

        for file in files_list:
            file_name = Path(file).stem
            file_suffix = Path(file).suffix

            if file_suffix in ['.wem', '.WEM']:

                make_directory(path = f'{output_path}')

                # Convert .WEM to .OGG
                ww2ogg_script = f'{self.ww2ogg_path} "{file}" --pcb {self.ww2ogg_codebooks_path} -o "{output_path}/{file_name}.ogg"'
                ww2ogg_output = run(args = ww2ogg_script, stderr = PIPE, stdout = DEVNULL)

                # Revorb the .OGG to get better quality
                revorb_script = f'{self.revorb_path} "{output_path}/{file_name}.ogg"'
                revorb_output = run(args = revorb_script, stderr = PIPE)


    def convert_to_wav(self, input_path: str) -> None:
        output_path = f'src/temp/converted/{Path(input_path).stem}'

        files_list = [file for file in Path(input_path).glob('*.ogg') if file.is_file()]

        for file in files_list:
            file_name = Path(file).stem

            ffmpeg_script = f'ffmpeg -hide_banner -nostdin -i "{file}" -acodec pcm_s16le -ar 44100 -y {output_path}/{file_name}.wav'
            ffmpeg_output = run(args = ffmpeg_script, stderr = PIPE)

            Path(file).unlink()


# HOW TO USE
'''
tools = Convert()
for folder in Path('src/temp/extracted').glob('*'):
    tools.convert_to_ogg(input_path = f'src/temp/extracted/{folder.name}')

for folder in Path('src/temp/converted').glob('*'):
    tools.convert_to_wav(input_path = f'src/temp/converted/{folder.name}')
'''
