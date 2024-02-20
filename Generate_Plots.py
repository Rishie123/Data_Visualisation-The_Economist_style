# Importing all the necessary libraries for the task

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
from pathlib import Path
import matplotlib.font_manager as fm

# Importing the data from WERD Dataset downloaded from Stanford Website( https://werd.stanford.edu/ )
data = pd.read_csv('WERD_Dataset.csv')

# Defining lists of countries for each region gotten from https://statisticstimes.com/geography/countries-by-continents.php
asia_countries = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
south_america_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
europe_countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City']
australia_countries = [ 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

# Filtering data for each contient in the dataset
data_asia = data[data['country_name'].isin(asia_countries)]
data_south_america = data[data['country_name'].isin(south_america_countries)]
data_europe = data[data['country_name'].isin(europe_countries)]
data_australia = data[data['country_name'].isin(australia_countries)]

# Calculating the number of reforms for top2 countries in the region
reforms_asia = data_asia.groupby('country_name').size().nlargest(2)
reforms_south_america = data_south_america.groupby('country_name').size().nlargest(2)
reforms_europe = data_europe.groupby('country_name').size().nlargest(2)
reforms_australia = data_australia.groupby('country_name').size().nlargest(2)

# Creating a DataFrame for the stacked bar chart
df = pd.DataFrame({
    'Asia': reforms_asia,
    'South America': reforms_south_america,
    'Europe': reforms_europe,
    'Australia': reforms_australia
}).fillna(0)

# Reordering columns for sorting legends by regions
df = df[['Asia', 'South America', 'Europe', 'Australia']]

# Defining the colors from the style guide
colors = ['#0c5193', '#0fb1c6', '#d6ad42']

# Loading the font defined in the style guide and downloaded from this github repository ( https://github.com/hrbrmstr/hrbrthemes)
font_path = "Econ_Sans_Font.ttf"
prop = fm.FontProperties(fname=font_path)

# Converting to px, as advised in the official doumentation for matplotlib and then plotting the graph
px = 1/plt.rcParams['figure.dpi']
ax = df.T.plot(kind='bar', stacked=True, figsize=(672*px, 400*px), color=colors)
ax.set_xlabel('Region', fontproperties=prop, fontsize=8, fontweight='bold')
ax.set_ylabel('Number of Reforms', fontproperties=prop, fontsize=8, fontweight='bold')
ax.set_xticklabels(ax.get_xticklabels(), fontproperties=prop, fontsize=8)

# Adding horizontal grid lines as in the style guide
ax.yaxis.grid(True)

# Adding a red rectangle at the top left corner touching the top of the chart as in the style guide
ax.add_patch(patches.Rectangle((0.02, 0.97), 0.04, 0.03, color='red', transform=ax.transAxes))

# Getting title inside the plot with some space from the top as required in the style guide
ax.text(0.4, 0.9, 'Highest no. of Education Reforms ', ha='right', fontproperties=prop, fontsize=10, fontweight='bold', transform=ax.transAxes)

# Getting legend outside as required in style guide
ax.legend(title='Top 2 countries', bbox_to_anchor=(1, 1), fontsize=8)

# Saving the plot as a figure in pdf format as required to have support vector graphics in the style guide
plt.savefig('Plots/Top-2-countries_by_region.pdf', bbox_inches='tight')

plt.show()



# Filtering data starting from the year 1900 and not exceeding 2024 ( For the sake of the plot )
data_asia = data_asia[(data_asia['year'] >= 1900) ]
data_europe = data_europe[(data_europe['year'] >= 1900) ]

# Grouping data by year and counting the number of reforms for each year
reforms_by_year_asia = data_asia.groupby('year').size()
reforms_by_year_europe = data_europe.groupby('year').size()

# Defining the colors from the style guide
colors = ['#0c5193', '#0fb1c6']

# Plotting the figure with the correct dimensions as required by the style guide.
fig, ax = plt.subplots(figsize=(672*px, 400*px))

# Loading the custom font Econ Sans, as required by the style guide.
font_path = "Econ_Sans_Font.ttf"
prop = fm.FontProperties(fname=font_path)

# Plot reforms in Asia as a line plot with specified color
plt.plot(reforms_by_year_asia.index, reforms_by_year_asia.values, label='Asia', color=colors[0])

# Plot reforms in Europe as a line plot with specified color
plt.plot(reforms_by_year_europe.index, reforms_by_year_europe.values, label='Europe', color=colors[1])

# Making only y-axis grid lines, as required by the style guide..
ax.yaxis.grid(True)

# Add a red brick at the top left corner touching the top of the chart as required by the stle guide
ax.add_patch(patches.Rectangle((0.02, 0.97), 0.04, 0.03, color='red', transform=ax.transAxes))

# Title inside the plot with some space from the top as required by the stle guide
ax.text(0.68, 0.9, 'Education Reforms over time in Asia vs Europe ', ha='right', fontproperties=prop, fontsize=14, fontweight='bold', transform=ax.transAxes)

plt.xlabel('Year', fontproperties=prop, fontsize=12, fontweight='bold')
plt.ylabel('Number of Reforms', fontproperties=prop, fontsize=12, fontweight='bold')

# Setting x-axis limits and tick labels
plt.xlim(1900, 2024)
plt.xticks(range(1900, 2025, 10), rotation=45)

plt.legend()
plt.tight_layout()
plt.savefig("Plots/reforms_over_time.pdf")
plt.show()

