# 1 
import pandas as pd

list = [1,2,3,4,5]
series = pd.Series(list)

print(series)

#============================================================================================#
# 2 

import pandas as pd

list = [1,2,3,4,5]
series = pd.Series(list)

new_list = series.tolist()

print(new_list)
print(type(new_list))

#============================================================================================#
# 3 

import pandas as pd

list1 = pd.Series([1,2,3,4,5])
list2 = pd.Series([2,4,6,8,10])

add = list1 + list2

subtract = list1 - list2

multiply = list1 * list2

divide = list1 / list2

print(add)
print(subtract)
print(multiply)
print(divide)

#============================================================================================#
# 4 

import pandas as pd

list1 = pd.Series([1,2,3,4,5])
list2 = pd.Series([7,'b',3,'d',5])

new_result = list1 == list2

print(new_result)

#============================================================================================#
# 5

import pandas as pd

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

series_dict = pd.Series(dict)

print(series_dict)

#============================================================================================#
# 6 

import pandas as pd
se3 = pd.Series([10, 20, 30, 40, 50])
ind = se3.loc[se3==30]
print(ind)

#============================================================================================#
# 7 

dataframe = pd.DataFrame(
    {'Letter': ['A','B','C'],
     'Num': [1,2,3],
     'Value': [100,200,300]} ).set_index(['Letter','Numb'])

print(dataframe)

fil_dataframe = dataframe.loc['B']
print(fil_dataframe)

#============================================================================================#
# 8 

import pandas as pd

dict = {'A': [10,20,30], 'C': [40,50,60], 'D': [70,80,90]}
dataframe = pd.DataFrame(dict)

dataframe.insert(3, 'E',[100,110,120])
print(dataframe)

#============================================================================================#
# 9 

import pandas as pd

dict = {'X': [78, 85, 96, 80, 86],'Y': [84, 94, 89, 83, 86],'Z': [86, 97, 96, 72, 83]}

dataframe = pd.DataFrame(dict)
print(dataframe)

#============================================================================================#
# 10

import pandas as pd

dict = {'co11': [1,2,3,4,5],'co12': [4,5,6,7,8],'co13': [7,8,9,0,1]}

dataframe = pd.DataFrame(dict)

new_row = {'co11': 10, 'co12': 11, 'co13': 12}

dataframe = dataframe._append(new_row, ignore_index=True)

print(dataframe)




#============================================================================================#
#============================================================================================#
#============================================================================================#
