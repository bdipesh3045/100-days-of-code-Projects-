from cProfile import label
from matplotlib import pyplot as plt
from matplotlib.lines import lineStyles
import random
# generating random dataset
set1=[]
set2=[]
def array_name(data):
    while len(data)!=12:
        data.append(random.randint(0,7675))
array_name(set1)
array_name(set2)
print(set1,set2)
x_axis="January, February, March, April, May, June, July, August, September, October, November, December"
x_axis=x_axis.split(',')
print(x_axis)

plt.plot(x_axis,set1,color="k",linestyle='--',marker='.',label="2021")
plt.plot(x_axis,set2,marker='o',label="2022")
plt.style.use("fivethirtyeight")

plt.xlabel("Months")
plt.ylabel("Cases per month")
plt.title("Covid 19 cases in the year 2021 and 2022")
plt.legend()
plt.tight_layout()
plt.grid(True)
# plot.savefig('plot.png')
# plt.xkcd()
plt.show()
