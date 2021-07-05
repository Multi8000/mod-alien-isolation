"""
STEP 04

This script will convert the modified .WAV files
into .WEM files

"""

from subprocess import (run, PIPE, DEVNULL)
from pathlib import Path

from __utils__ import make_directory


class Convert():

    def __init__(self):
        self.wwise_cli_path = 'C:/Program Files (x86)/Audiokinetic/Wwise 2021.1.1.7601/Authoring/x64/Release/bin/WwiseCLI.exe'
        #self.wwise_xml_sources_path = 'src/temp/list.wsources'
        self.wwise_project_path = 'src/tools/Wwise/mod-alien-isolation/mod-alien-isolation.wproj'


    def generate_xml_sources(self, input_path: str) -> None:
        output_path = f'src/temp/normalized/{Path(input_path).stem}/list.wsources'

        files_list = [file for file in Path(input_path).glob('*.wav') if file.is_file()]

        with open(file = output_path, mode = 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(f'<ExternalSourcesList SchemaVersion="1" Root="{Path(input_path).resolve()}">\n')

            for file in files_list:
                f.write(f'\t<Source Path="{Path(file).resolve()}" Conversion="Vorbis Quality High" />\n')

            f.write("</ExternalSourcesList>")


    def convert_to_wem(self, wwise_xml_sources: str) -> None:
        output_path = make_directory(path = f'src/temp/modified/{Path(wwise_xml_sources).parent.stem}')

        script = f'"{self.wwise_cli_path}" "{self.wwise_project_path}" -ConvertExternalSources "{wwise_xml_sources}" -ExternalSourcesOutput "{Path(output_path).resolve()}"'
        script_output = run(args = script, stderr = PIPE, stdout = DEVNULL)


# HOW TO USE
'''
tools = Convert()
for folder in Path('src/temp/normalized').glob('*'):
    tools.generate_xml_sources(input_path = f'src/temp/normalized/{folder.name}')

for folder in Path('src/temp/normalized').glob('*'):
    for file in Path(folder).glob('*.wsources'):
        tools.convert_to_wem(wwise_xml_sources = Path(file).resolve())

'''
