import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-08-22/population.csv')
df[df['year'] == 2022].to_csv('refugee_2022.csv', index = False)