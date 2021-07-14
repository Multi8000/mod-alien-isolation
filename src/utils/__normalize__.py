"""
STEP 03

This script will normalize the .WAV files loudness

"""

from subprocess import (run, PIPE, DEVNULL)
from pathlib import Path
import pandas

from __utils__ import make_directory


normalize_script = Path('../auto-2pass-loudnorm/normalize.py').resolve()


# Read .csv
dataframe = pandas.read_csv('src/audio_changes.csv')

# Manual audio changes that isn't possible to automate
manual_audio_name_mods = ['SPOT_Cat_RunAway_BB_B_01',
                          'SPOT_Cat_Pur_BB_A_04',
                          'SPOT_Cat_Pur_BB_A_03',
                          'SPOT_Cat_Pur_BB_A_01',
                          'SPOT_Cat_Pur_BB_A_02',
                          'A1_M0701_VER_5927',
                          'A1_M1404_SGF_6441']

# Removes the manual audio changes from the dataframe
dataframe = dataframe[~dataframe['audio_name'].isin(manual_audio_name_mods)].reset_index()

# Iterate over dataframe to capture variables for the normalize script
for index, row in dataframe.iterrows():
    input_file = f''
    desired_lufs = row['desired_lufs']
    output_folder = f''

    #script = f'python.exe "{normalize_script}" -file "/mod-alien-isolation/100184715.wav" -lufs {desired_lufs} -output {output_folder}'
    #script_output = run(args = script, stderr = PIPE, shell = True)
    print(row['soundbank_name'].split(sep = '.')[0])
