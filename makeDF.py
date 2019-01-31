#! /usr/bin/env python3

import pandas as pd

artists = ["50_cent","21_savage","B-Real","Machine_Gun_Kelly","Eminem","Snoop_Dogg","Nicki Minaj","Tyler, The Creator","Dj_Khaled","Migos","Kendrick_Lamar","Lil_Peep","Lil_Pump","Lil_Wayne","Lil_Uzi_Vert","Soulja_Boy"]

data = {'Number of Words': [254388, 31023, 6981, 68818, 393558, 256696, 131489, 44263, 108580, 87143, 84223, 6222, 9190, 521529, 34362, 76853],
        'Number of slangs': [7922,   1466, 154,  1575,  10513, 7083, 3430, 1781, 2593, 2500, 2286, 115, 326, 16641, 941, 1805],
        'Average of words until a slang': [32, 21, 45, 43, 37, 36, 38, 24, 41, 34, 36, 54, 28, 31, 36, 42]}

df = pd.DataFrame(data, 
        columns = ["Number of Words","Number of slangs","Average of words until a slang"],
        index = artists
        )

print(df.to_string())
