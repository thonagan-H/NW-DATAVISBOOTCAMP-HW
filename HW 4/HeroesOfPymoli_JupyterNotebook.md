

```python
import pandas as pd
import numpy as np
```


```python
data_file = "purchase_data.json"
```


```python
data_file_pd = pd.read_json(data_file)
data_file_pd.head(12)
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Chamosia29</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Sally64</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Total number of players in the dataframe
unique_names = data_file_pd["SN"].unique()
unique_name_count = len(unique_names)

```


```python
#Purchasing analysis - Number of unique items
num_unique_items = data_file_pd["Item Name"].value_counts()
#new_df = data_file_pd.groupby("Item Name")
#new_df.size()
```


```python
#Purchasing Analysis - Price Mean:
data_file_pd["Price"].mean()
```




    2.931192307692303




```python
#Purchasing Analysis - Total Number of Purchases
num_unique_items.count()
```




    179




```python
#Purchasing Analysis - Total Revenue
data_file_pd["Price"].sum()
```




    2286.3299999999999




```python
#Gender Demographics - Percentage and count of male players:
gender_vals = data_file_pd["Gender"].value_counts()
total_players = gender_vals.sum()
gender_m_count = gender_vals.values[0]
gender_f_count = gender_vals.values[1]
gender_o_count = gender_vals.values[2]
percentages_m = (gender_m_count/total_players)*100
percentages_f = (gender_f_count/total_players)*100
percentages_o = (gender_o_count/total_players)*100
gender_m_count

```




    633




```python
#Purchase Count: 
gender_purchase_count = data_file_pd.groupby(["Gender"])["Price"].count()

#Average price of individual player by gender
gender_player_items_count = data_file_pd.groupby(["Gender","SN"])["Price"].count()
gender_player_items_sum = data_file_pd.groupby(["Gender","SN"])["Price"].sum()
gender_player_items_avg = gender_player_items_sum/gender_player_items_count

#total value of goods by gender
gender_tot_val = data_file_pd.groupby(["Gender"])["Price"].sum()

#Normalized Total
norm_tot_gender = gender_purchase_count/gender_vals
gender_tot_val

```




    Gender
    Female                    382.91
    Male                     1867.68
    Other / Non-Disclosed      35.74
    Name: Price, dtype: float64




```python
#bins
#I thought about using the range function with the intital value set at 1 less than age_min 
#and the final value set at 1 greater than age_max for the bins, but I was unable to figure out how to label these bins without
#hard coding them in

age_max = data_file_pd["Age"].max()
age_min = data_file_pd["Age"].min()
bins = [age_min-1,10,14,19,24,29,34,39,44,age_max+1]
bin_range = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40-44","45-49"]
data_file_pd["Age Bins"] = pd.cut(data_file_pd["Age"],bins,labels = bin_range)

#Purchase Count
age_purchase_count = data_file_pd.groupby(["Age Bins"]).count()


#Total Purchase Value
age_tot_purchase_val = data_file_pd.groupby(["Age Bins"])["Price"].sum()

#Average purcahse price of each player by age
age_player_items_count = data_file_pd.groupby(["Age Bins","SN"])["Price"].count()
age_player_items_sum = data_file_pd.groupby(["Age Bins","SN"])["Price"].sum()
age_player_items_avg = age_player_items_sum/age_player_items_count

#Normalized Total 
norm_tot_age = age_tot_purchase_val/age_purchase_count["Price"]
age_purchase_count

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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
    <tr>
      <th>Age Bins</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
      <td>31</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>133</td>
      <td>133</td>
      <td>133</td>
      <td>133</td>
      <td>133</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>336</td>
      <td>336</td>
      <td>336</td>
      <td>336</td>
      <td>336</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
      <td>125</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>42</td>
      <td>42</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>16</td>
      <td>16</td>
      <td>16</td>
      <td>16</td>
      <td>16</td>
      <td>16</td>
    </tr>
    <tr>
      <th>45-49</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Spenders 
ts_tot_price = data_file_pd.groupby(["SN"])["Price"].sum()
ts_item_count = data_file_pd.groupby(["SN"])["Price"].count()
ts_avg_price = ts_tot_price/ts_item_count

ts_df = ts_tot_price.to_frame(name="Total Purchase Amount")
ts_df["item count"] = ts_item_count.values
ts_df["avg price"] = ts_avg_price
sorted_ts_df = ts_df.sort_values("Total Purchase Amount",ascending = False)
sorted_ts_df.head(5)
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
      <th>Total Purchase Amount</th>
      <th>item count</th>
      <th>avg price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>3.412000</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>3.390000</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>3.185000</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>4.243333</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>3.860000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Items by purchase count
ti_purchase_count = data_file_pd.groupby(["Item Name"])["Price"].count()
ti_purchase_value = data_file_pd.groupby(["Item Name"])["Price"].sum()
ti_item_price = ti_purchase_value/ti_purchase_count

ti_df = ti_purchase_value.to_frame(name="Total Purchase Value")
ti_df["item count"] = ti_purchase_count.values
ti_df["Price"] = ti_item_price.values
sorted_ti_df = ti_df.sort_values("item count",ascending = False)
sorted_ti_df.head(5)
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
      <th>Total Purchase Value</th>
      <th>item count</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>38.60</td>
      <td>14</td>
      <td>2.757143</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <td>24.53</td>
      <td>11</td>
      <td>2.230000</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>25.85</td>
      <td>11</td>
      <td>2.350000</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>34.65</td>
      <td>10</td>
      <td>3.465000</td>
    </tr>
    <tr>
      <th>Woeful Adamantite Claymore</th>
      <td>11.16</td>
      <td>9</td>
      <td>1.240000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Items by purchase value
sorted_ti_df_pv = ti_df.sort_values("Total Purchase Value",ascending = False)
sorted_ti_df_pv.head(5)
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
      <th>Total Purchase Value</th>
      <th>item count</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>38.60</td>
      <td>14</td>
      <td>2.757143</td>
    </tr>
    <tr>
      <th>Retribution Axe</th>
      <td>37.26</td>
      <td>9</td>
      <td>4.140000</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>34.65</td>
      <td>10</td>
      <td>3.465000</td>
    </tr>
    <tr>
      <th>Spectral Diamond Doomblade</th>
      <td>29.75</td>
      <td>7</td>
      <td>4.250000</td>
    </tr>
    <tr>
      <th>Orenmir</th>
      <td>29.70</td>
      <td>6</td>
      <td>4.950000</td>
    </tr>
  </tbody>
</table>
</div>


