import pandas as pd
import numpy as nump
import glob as g
import matplotlib.pyplot as plt
# Lets doooo thiiissss

# adding up al teh csv files into one
# BUT FIRST , we must make sure to load em up together to see them at once , using a loop with glob
# glob helps reiterate through file with matching pattern, * means match zero or more characters , ? : exactly one character

# lets do sum globbing
all_states_csv = g.glob("*.csv")

# gotta shove the csv shtuff up in a dataframe

us_census = pd.DataFrame()

for file in all_states_csv:
    raw = pd.read_csv(file)
    us_census = pd.concat([us_census, raw], ignore_index=True)

us_census.to_csv("us_census.csv", index=False)
# successfully created one jumbo file , still imperfect but we love her
# lets take her to the SALON to clean and tidy up!

# look at her head, will print 10 rows topmost
print(us_census.head(), "\n\n")

# now we gotta clean her up for real real, manipulating data types and replacing odd symbols such as $ , column wise ofc
# sum external typecasting action goin on over here

us_census['Asian'] = pd.to_numeric(us_census['Asian'].str.replace('%', ''))
us_census['Hispanic'] = pd.to_numeric(us_census['Hispanic'].str.replace('%', ''))
us_census['Income'] = pd.to_numeric(us_census['Income'].replace('\$', '', regex=True))
us_census['Pacific'] = pd.to_numeric(us_census['Pacific'].str.replace('%', ''))
us_census['White'] = pd.to_numeric(us_census['White'].str.replace('%', ''))
us_census['Black'] = pd.to_numeric(us_census['Black'].str.replace('%', ''))
us_census['Native'] = pd.to_numeric(us_census['Native'].str.replace('%', ''))


us_census.reset_index(drop=True)
# gotta split her up , by her I meant the genderpopulation men and wamen
us_census[['men', 'women']] = us_census['GenderPop'].str.split('_', expand=True)

# remove M and F char tyme for converting to its right type
# gotta strip using str.split
# str.split() is a method of string class that is used to split a string into a list, expand=True means expand the split strings into separate columns
us_census['men'] = pd.to_numeric(us_census['men'].str.replace('[,M]', '', regex=True))
us_census['women'] = pd.to_numeric(us_census['women'].str.replace('[,F]', '', regex=True))

# plt.scatter(the_women_column, the_income_column) Remember to call the alias to show

x = us_census['women']
y = us_census['men']
plt.scatter(x, y)
plt.show()


# printing out the duplicated columns in wamen to see which oens messing us up
# filling nan value in column women with total pop per state minus men per state
us_census['women'] = us_census['women'].fillna(us_census['TotalPop'] - us_census['men'])
print(us_census.duplicated().value_counts())
us_census = us_census.drop_duplicates()
us_census.dropna()

print(us_census.isnull(), "\n\n")

print(pd.read_csv('us_census.csv'), "\n\n")
print(us_census['women'], "\n\n")


# graph 1 , average income in a state vs the [rp[pstion of women in that state

plt.scatter(us_census['women']/us_census['TotalPop'], us_census['Income'])
plt.xlabel('wamen Props')
plt.ylabel('avg income')
plt.show()

# making histograms of race data in each race , lets do thiss , in seperate files you can checky
plt.hist(us_census['Asian'], color = 'red')
plt.xlabel('Percentage of Asian Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Black'], color = 'pink')
plt.xlabel('Percentage of Black Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['White'], color='yellow')
plt.xlabel('White Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Native'], color='brown')
plt.xlabel('%age of Native Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Hispanic'], color='purple')
plt.xlabel('Hispanic Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Pacific'], color='green')
plt.xlabel('Pacific Population')
plt.ylabel('count')
plt.show()

# handling missing data like the void in my heartthu

us_census = us_census.fillna(value={'Asian': 0, 'Black': 0, 'White': 0, 'Pacific': 0, 'Hispanic': 0, 'Native': 0})

