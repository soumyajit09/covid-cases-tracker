# Importing required libraries
from covid import Covid
import matplotlib.pyplot as plt

covid = Covid()

# getting Country Name
country_name = input("Enter the Country Name : ")

# getting data of country using country name
virus_data = covid.get_status_by_country_name(country_name)

# removing the key values that are not required
remove = ['id', 'country', 'latitude', 'longitude', 'last_update']
for i in remove:
    virus_data.pop(i)

# getting no of confirmed cases
confirmed_cases = virus_data.pop('confirmed')

# getting all keys
keys = list(virus_data.keys())

# getting all key values
values = [str(i) for i in virus_data.values()]

# visualizing the data
plt.pie(values, labels=keys, colors=['r', 'y', 'g', 'b'], autopct="%1.2f%%")
plt.title("COUNTRY : "+country_name.upper()+" \n Total Cases : "+str(confirmed_cases))
fig = plt.gcf()
fig.canvas.set_window_title('Covid Tracker')
plt.legend()
plt.show()
