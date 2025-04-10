---
layout: post
title: Lists and Filtering HW
description: 
type: issues
comments: True
---
## Popcorn Hack 1


```python
import pandas as pd


def find_students_in_range(df, min_score, max_score):
    return df[(df['Score'] >= min_score) & (df['Score'] <= max_score)]

student_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Score': [85, 92, 78, 88]
})

find_students_in_range(student_data, 80, 90)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>85</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Diana</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
</div>



## Popcorn Hack 2


```python
def add_letter_grades(df):
    def get_letter(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    df['Letter'] = df['Score'].apply(get_letter)
    return df


import pandas as pd

student_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Score': [85, 92, 78, 59]
})

add_letter_grades(student_data)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Score</th>
      <th>Letter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>85</td>
      <td>B</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>92</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>78</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Diana</td>
      <td>59</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>



## Popcorn Hack 3


```python
def find_mode(series):
    return series.mode().iloc[0]

import pandas as pd

find_mode(pd.Series([1, 2, 2, 3, 4, 2, 5]))

```




    np.int64(2)




```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import folium

# Load data
data = pd.read_csv('/home/shawnray/nighthawk/shawnr_2025/datasets/treas_parking_meters_loc_datasd.csv')
data.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>zone</th>
      <th>area</th>
      <th>sub_area</th>
      <th>pole</th>
      <th>config_id</th>
      <th>config_name</th>
      <th>date_inventory</th>
      <th>lat</th>
      <th>lng</th>
      <th>sapid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Downtown</td>
      <td>Core</td>
      <td>1000 FIRST AVE</td>
      <td>1-1004</td>
      <td>49382</td>
      <td>Sunday Mode</td>
      <td>2021-01-04 00:00:00</td>
      <td>32.715904</td>
      <td>-117.163929</td>
      <td>SS-000031</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Downtown</td>
      <td>Core - Columbia</td>
      <td>1000 FIRST AVE</td>
      <td>1-1004</td>
      <td>9000</td>
      <td>2 Hour Max $1.25 HR 8am-6pm Mon-Sat (NFC)</td>
      <td>2018-11-11 00:00:00</td>
      <td>32.715904</td>
      <td>-117.163929</td>
      <td>SS-000031</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Downtown</td>
      <td>Core</td>
      <td>1000 FIRST AVE</td>
      <td>1-1006</td>
      <td>49382</td>
      <td>Sunday Mode</td>
      <td>2021-01-04 00:00:00</td>
      <td>32.716037</td>
      <td>-117.163930</td>
      <td>SS-000031</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Downtown</td>
      <td>Core - Columbia</td>
      <td>1000 FIRST AVE</td>
      <td>1-1006</td>
      <td>9000</td>
      <td>2 Hour Max $1.25 HR 8am-6pm Mon-Sat (NFC)</td>
      <td>2018-11-11 00:00:00</td>
      <td>32.716037</td>
      <td>-117.163930</td>
      <td>SS-000031</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Downtown</td>
      <td>Core</td>
      <td>1000 FIRST AVE</td>
      <td>1-1008</td>
      <td>49382</td>
      <td>Sunday Mode</td>
      <td>2021-01-04 00:00:00</td>
      <td>32.716169</td>
      <td>-117.163931</td>
      <td>SS-000031</td>
    </tr>
  </tbody>
</table>
</div>




```python
zone_counts = data['zone'].value_counts()

plt.figure(figsize=(10, 6))
zone_counts.plot(kind='bar', color='teal')
plt.title('Number of Meters per Zone')
plt.xlabel('Zone')
plt.ylabel('Number of Meters')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```


    




<img src="{{site.baseurl}}/images/output3.png" width="900" alt="postmanget">



```python
area_counts = data['area'].value_counts().sort_values(ascending=False)
sub_area_counts = data['sub_area'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
area_counts.plot(kind='bar', color='orange')
plt.title('Number of Meters per Area')
plt.xlabel('Area')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```



    




<img src="{{site.baseurl}}/images/output2.png" width="900" alt="postmanget">



```python
data['date_inventory'] = pd.to_datetime(data['date_inventory'], errors='coerce')
data['inventory_year'] = data['date_inventory'].dt.year

year_counts = data['inventory_year'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
year_counts.plot(kind='bar', color='purple')
plt.title('Number of Meters Installed by Year')
plt.xlabel('Year')
plt.ylabel('Number of Meters')
plt.tight_layout()
plt.show()

```



    



<img src="{{site.baseurl}}/images/output.png" width="900" alt="postmanget">




```python
# Top 10 most common configurations
top_configs = data['config_name'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_configs.index, y=top_configs.values, palette='viridis')

plt.title('Top 10 Most Common Parking Meter Configurations')
plt.xlabel('Configuration Name')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Tilt the x-axis labels
plt.tight_layout()
plt.show()

```

    /tmp/ipykernel_1014/91221402.py:5: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.barplot(x=top_configs.index, y=top_configs.values, palette='viridis')



    



<img src="{{site.baseurl}}/images/output1.png" width="900" alt="postmanget">



```python
map_sd = folium.Map(location=[data['lat'].mean(), data['lng'].mean()], zoom_start=13)

for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lng']],
        radius=2,
        popup=f"Pole: {row['pole']}<br>Zone: {row['zone']}",
        color='blue',
        fill=True,
        fill_opacity=0.5
    ).add_to(map_sd)

# Show in Jupyter OR save to HTML
map_sd.save('smartpark_map.html')


```


```python
conn = sqlite3.connect('smartpark_inventory.db')
data.to_sql('meter_inventory', conn, if_exists='replace', index=False)

```




    10964




```python
query1 = """
SELECT zone, COUNT(*) AS meter_count
FROM meter_inventory
GROUP BY zone
ORDER BY meter_count DESC;
"""
pd.read_sql(query1, conn)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>zone</th>
      <th>meter_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Downtown</td>
      <td>6196</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Uptown</td>
      <td>4017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mid-City</td>
      <td>548</td>
    </tr>
    <tr>
      <th>3</th>
      <td>City</td>
      <td>155</td>
    </tr>
    <tr>
      <th>4</th>
      <td>San Diego, CA Default Zone</td>
      <td>48</td>
    </tr>
  </tbody>
</table>
</div>




```python
query2 = """
SELECT config_name, MIN(date_inventory) as first_seen, MAX(date_inventory) as last_seen
FROM meter_inventory
GROUP BY config_name;
"""
pd.read_sql(query2, conn)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>config_name</th>
      <th>first_seen</th>
      <th>last_seen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 Hour Max $1.25 HR 10am-8pm Mon-Sat (Mobile P...</td>
      <td>2018-11-11 00:00:00</td>
      <td>2021-03-23 00:00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1 Hour Max $1.25 HR 8am-4pm Mon-Fri 8am-6pm Sa...</td>
      <td>2018-11-11 00:00:00</td>
      <td>2018-11-11 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1 Hour Max $1.25 HR 8am-4pm Mon-Sat (NFC)</td>
      <td>2018-11-11 00:00:00</td>
      <td>2018-11-11 00:00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1 Hour Max $1.25 HR 8am-5pm Mon-Sat, No Parkin...</td>
      <td>2018-11-11 00:00:00</td>
      <td>2018-11-11 00:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1 Hour Max $1.25 HR 8am-6pm Mon-Sat (Mobile Pa...</td>
      <td>2018-11-11 00:00:00</td>
      <td>2020-02-02 00:00:00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>105</th>
      <td>MSPM-PBS 2 Hour Max $1.25 HR 10am-8pm Mon-Sat</td>
      <td>2019-12-29 00:00:00</td>
      <td>2019-12-29 00:00:00</td>
    </tr>
    <tr>
      <th>106</th>
      <td>San Diego Default</td>
      <td>2018-11-11 00:00:00</td>
      <td>2019-12-29 00:00:00</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Single Space 2 hour meters Petco Special Event...</td>
      <td>2019-12-29 00:00:00</td>
      <td>2022-09-12 00:00:00</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Single Space 30 min meters Petco Special Event...</td>
      <td>2019-12-29 00:00:00</td>
      <td>2019-12-29 00:00:00</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Sunday Mode</td>
      <td>2021-01-04 00:00:00</td>
      <td>2021-01-04 00:00:00</td>
    </tr>
  </tbody>
</table>
<p>110 rows × 3 columns</p>
</div>



### Comparison: SQL vs Pandas

- **Pandas Pros**: Easy chaining, good for rapid prototyping, integrates with plotting libraries.
- **SQL Pros**: Declarative, familiar to database users, better for large structured queries.
- **Pandas Cons**: Can get messy with complex filters or joins.
- **SQL Cons**: Harder to visualize data, more verbose syntax for basic operations.

In this project, Pandas was great for quick aggregation and plotting, while SQL was useful for queries like counting meters per zone or filtering by date.

