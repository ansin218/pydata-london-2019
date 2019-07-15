import os

from os.path import splitext, basename

import pandas as pd

WANTED_COLS = ['Date', 'Hour', 'User Name', 'Tweet content', 'Is a RT', 'RTs']
xl = [file for file in os.listdir('tweets') if file.endswith('.xlsx')]

for file in xl:
	print(f'Converting {basename(file)}')
	df = pd.read_excel(f'tweets/{file}', sheet_name='Stream')
	df = df[WANTED_COLS]
	df.to_csv(f'tweets/{basename(splitext(file)[0])}.csv')
