"""
STEP 01

This script will generate a folder with the internal .WEM and .DAT files
and a .TXT list with the name of these files.

We will use this folder to put the modified .WEM files
and rebuild the .PCK or .BNK file.

"""

from subprocess import (run, PIPE)
from pathlib import Path

from __utils__ import make_directory


class Extract():

    def __init__(self):
        self.rscanner_path = 'src/tools/RavioliGameTools/RScannerConsole.exe'
        self.output_path = 'src/temp/extracted'


    def generate_internal_file_name_list(self, input_path):

        files_list = [file for file in Path(input_path).glob('*') if file.is_file()]

        for file in files_list:
            if Path(file).suffix in ['.BNK', '.PCK']:

                file_name = Path(file).stem
                output_path = Path(f'{self.output_path}/{file_name}/{file_name}.txt')

                make_directory(path = f'{self.output_path}/{file_name}')

                script = f'''"{self.rscanner_path}" "{file}" /list > "{output_path}"'''
                script_output = run(args = script, stderr = PIPE, shell = True)


    def extract_from_pck_bnk(self, input_path):

        files_list = [file for file in Path(input_path).glob('*') if file.is_file()]

        for file in files_list:
            if Path(file).suffix in ['.BNK', '.PCK']:

                file_name = Path(file).stem
                output_path = Path(f'{self.output_path}/{file_name}')

                script = f'''"{self.rscanner_path}" "{file}" /extract:"{output_path}" /unknowns'''
                script_output = run(args = script, stderr = PIPE, shell = True)


# HOW TO USE
'''
tools = Extract()
tools.generate_internal_file_name_list('src/temp/original/banks')
tools.extract_from_pck_bnk('src/temp/original/banks')

'''
