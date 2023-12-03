import pandas as pd

def region(params):
    geo_data = {
        'Центр': ['москва', 'тула', 'ярославль'],
        'Северо-Запад': ['петербург', 'псков', 'мурманск'],
        'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
    }

    words = params.keyword.split(' ')

    for word in words:
        for region in geo_data:
            if word.lower() in geo_data[region]:
                return region

    return 'undefined'

keywords = pd.read_csv("./keywords.csv")
keywords['region'] = keywords.apply(region, 1)
keywords.to_csv('output.csv')

print(keywords)

"""
Output:
                       keyword     shows     region
0                           вк  64292779  undefined
1                одноклассники  63810309  undefined
2                        порно  41747114  undefined
3                         ютуб  39995567  undefined
4                    вконтакте  21014195  undefined
...                        ...       ...        ...
99995   эльдорадо старый оскол      3705  undefined
99996      frigate для firefox      3630  undefined
99997                   укрсиб      3630  undefined
99998  погода в ялте на неделю      3688  undefined
99999                     ггму      3630  undefined

[100000 rows x 3 columns]

Classified examples from 'output.csv':
6075,ярославль,41720,Центр
8977,мурманск,29984,Северо-Запад
9084,хабаровск,29655,Дальний Восток
"""

