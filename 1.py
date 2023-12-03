import pandas as pd

def classification(param):
    if param.avg_rate <= 2:
        return 'низкий рейтинг'
    elif param.avg_rate < 4.5:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'


ratings = pd.read_csv('./ratings.csv')
movies = pd.read_csv('./movies.csv')
movies = ratings[ratings.rating == 5].join(movies.set_index('movieId'))
avg_rates = ratings.groupby('movieId').rating.mean()
result = movies.merge(avg_rates.rename('avg_rate'), left_index=True, right_index=True)
result['class'] = result.apply(classification, 1)


print(result)

'''
Output:
       userId  movieId  rating   timestamp                                              title                                  genres  avg_rate            class
21          2       17     5.0   835355681                                  Get Shorty (1995)                   Comedy|Crime|Thriller  3.536842  средний рейтинг
22          2       39     5.0   835355604                                     Copycat (1995)     Crime|Drama|Horror|Mystery|Thriller  3.355263  средний рейтинг
29          2      150     5.0   835355395  City of Lost Children, The (Cité des enfants p...  Adventure|Drama|Fantasy|Mystery|Sci-Fi  4.025000  средний рейтинг
37          2      222     5.0   835355840                      Across the Sea of Time (1995)                        Documentary|IMAX  2.000000   низкий рейтинг
44          2      265     5.0   835355697                               Mortal Kombat (1995)                Action|Adventure|Fantasy  2.697368  средний рейтинг
...       ...      ...     ...         ...                                                ...                                     ...       ...              ...
99468     665     2141     5.0   992909251                      Central Park Five, The (2012)                             Documentary  2.500000  средний рейтинг
99728     666      590     5.0   838920789                              Gangster Squad (2013)                      Action|Crime|Drama  3.375000  средний рейтинг
99741     667       41     5.0   847271721                       Company You Keep, The (2012)                                Thriller  3.500000  средний рейтинг
99764     667      307     5.0   847271773                   It's Such a Beautiful Day (2012)   Animation|Comedy|Drama|Fantasy|Sci-Fi  5.000000  высокий рейтинг
99912     671     1136     5.0  1064891032                                        Mama (2013)                                  Horror  2.500000  средний рейтинг

[1196 rows x 8 columns]
'''
