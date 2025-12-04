import pandas as pd
import matplotlib.pyplot as plt

my_list = [1, 7, 2]
my_serie = pd.Series(my_list, index = ["x", "y", "z"])

print(my_serie["z"])

# --------------------

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

my_data_frame = pd.DataFrame(data)

print(my_data_frame.loc[[0, 1]])

# --------------------

my_data_frame_from_csv = pd.read_csv("example.csv")

print(my_data_frame_from_csv.loc[range(1, 4)])

# --------------------

my_data_frame_from_xlsx = pd.read_excel("example.xlsx")

print(my_data_frame_from_xlsx.loc[range(1, 4)])

# -----------------------

my_data_frame_from_xlsx.plot()
plt.show()
