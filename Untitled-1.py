# %%
import math
import numpy as np
import pandas as pd

# %%
def get_probability(event_info):
  SUM = sum(event_info)
  for i in range(len(event_info)):
        event_info[i] /= SUM
  return event_info


def get_entropy(event_info):
  probabilities = get_probability(event_info)
  entropy = 0.0
  for p in probabilities:
    if p != 0:
      entropy += p * math.log(1 / p) / math.log(2)
  return entropy


# %%
def sort_table_by_column(table, col):
    return table[table[:, col].argsort()]

# %%
example_dataset = dataset1 = pd.read_csv(r"example_data.csv")

# %%
print(example_dataset)

# %%
def split_dataset_wrt_column(dataset, column_name):
  unique_items = dataset[column_name].unique()
  for item in unique_items:
    yield dataset[dataset[column_name] == item]

# %%
class node:
  def __init__(self):
    self.table = None
    self.spliting_feature = None
    self.childs = []
  def add_child(self, child):
    self.childs.append(child)

# %%
def get_count(table, target_column, class_name):
  ans =  (table[target_column] == class_name).shape[0]
  # print (ans)
  return ans

# %%
def get_entropy_from_table(table, target_column):
  unique_classes = table[target_column].unique()
  # print(unique_classes)
  counts = []
  for class_name in unique_classes:
    counts.append(get_count(table,target_column, class_name))
  print("Count is ", counts)
  return get_entropy(counts)
  

# %%
def get_information_gain(dataset, column, target_column):
  tables = []
  size_table = []
  overall_size = dataset.shape[0]
  for table in split_dataset_wrt_column(dataset, column):
    tables.append(table)
    size_table.append(table.shape[0])
  entropies = []
  for table in tables:
    print(table)
    entropies.append(get_entropy_from_table(table, target_column))
  # print(entropies)
  # entropies = [get_entropy_from_table(table, target_column) for table in tables]
  # print(entropies)
  # entropy = sum([(size / overall_size) * entropyi for size, entropyi in zip(sizes, entropies)])
  # return entropy


# %%
get_information_gain(example_dataset, 'Outlook', 'target')

# %%


# %%



