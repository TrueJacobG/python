import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from os import environ

# remove warnings with matplotlib


def removeProblems():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


removeProblems()


# create screen -> if you want to make different graph
# in the future
plt.figure(0)


# create plot
x = [1, 2, 3]
y = [4, 5, 8]
plt.plot(x, y)

# create another plot
z = [10, 5, 2]
plt.plot(x, z)

# options
plt.title("Testing plot")
plt.xlabel("X")
plt.ylabel("Y AND Z")
plt.legend(["this is blue - Y", "this is orange - Z"])

# show plot
# plt.show()
# close showed graph
plt.close()


###################################

# with pandas
simple_data = pd.read_csv("sample_data.csv")

print(simple_data)

# print single column by using its name
print(simple_data.column_c)

# second row
print(simple_data.iloc[1])

###################################

# another graph
plt.figure(1)

# lines -> dotes
plt.plot(simple_data.column_a, simple_data.column_b, "o")
plt.plot(simple_data.column_a, simple_data.column_c)
# plt.show()
plt.close()

###################################

countries_data = pd.read_csv("countries.csv")

# print only with this country name
print(countries_data[countries_data.country == "United Kingdom"])

# Compare 2 populations
uk = countries_data[countries_data.country == "United Kingdom"]
norway = countries_data[countries_data.country == "Norway"]

plt.figure(2)
#plt.plot(uk.year, uk.population//10**6)
#plt.plot(norway.year, norway.population//10**6)

plt.plot(uk.year, uk.population/uk.population.iloc[0]*100)
plt.plot(norway.year, norway.population/norway.population.iloc[0]*100)

plt.legend(["United Kingdom", "Norway"])
plt.xlabel("Year")
plt.ylabel("Population growth")
plt.show()
