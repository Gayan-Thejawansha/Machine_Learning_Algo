#import matplotlib
#import matplotlib .pyplot as plt
import numpy as np
import pandas as pd


s = pd.Series([2,4,1,-4,'home'], index =['a', 'b', 'c', 'd', 'e'])

import pandas as pd
numbers = {1,2,3,4,5}
ser = pd.Series(list(numbers))

print(s)
print(ser)

data = {'population': [1.5 , 1.7, 3.6, 2.4, 2.9] ,
'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000 , 2001 , 2002 , 2001 , 2002]}
df = pd. DataFrame (data , columns =['year', 'state', 'population',
'debt'], index =['one', 'two', 'three', 'four', 'five'])
