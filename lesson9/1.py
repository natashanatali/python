import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

new_data = pd.DataFrame(dict.fromkeys(list(set(lst)), lst))


def set_one_hot(row):
    for element in new_data.columns:
        if row[element] == element:
            row[element] = 1
        else:
            row[element] = 0
    return row


new_data = new_data.assign().apply(set_one_hot, axis=1)
data = pd.concat([data, new_data], axis=1, join='inner')
data = data.drop(axis=1, columns=data.columns[0])
print(data)
