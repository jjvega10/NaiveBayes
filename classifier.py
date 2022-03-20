import pandas as pd

# Replace with your csv
df = pd.read_csv("bayestest.csv", header=None)

# Just to rename columns, depends on header, may need more names
#df = df.rename(columns={0:'First', 1:'Second', 2:'Third', 3:'Target'})

## Replace 'Target with column name of target'
target_name = 'Target'
# Replace 'test' with PD series that wants to be predicted
test = df.loc[0, df.columns != target_name]

classes = df[target_name].unique()

for target in classes:
    print(target)
    target_prob = []
    for column in df.columns:
        if column != target_name:
            class_mask = df.loc[:, target_name]==target
            column_mask = df.loc[:, column]==test[column]
            total_pos = df[class_mask][column].size
            my_pos = df[class_mask&column_mask][column].size
            target_prob.append(my_pos/total_pos)
            print(target_name + ' ' + str(target) + ', Column ' + str(column) + ", prob: " + str(my_pos/total_pos))
    result_for_class = 1
    for prob in target_prob:
        result_for_class = result_for_class * prob
    print('Probability of class ' + str(target) + ' is ' + str(result_for_class))
