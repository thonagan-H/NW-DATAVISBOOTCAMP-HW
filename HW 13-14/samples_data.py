import pandas as pd
import numpy as np
import csv

df_samples = pd.read_csv("belly_button_biodiversity_samples.csv")

#Sample_Values list with Otu_Ids and corresponding values
cols = df_samples.columns.tolist()
sample_vals_list = []

for i in cols:
    otu_id_list = []
    otu_id_vals = []
    
    for j in range(len(df_samples[i].values)):
        
            if  df_samples[i].values[j] > 0:
                               
                otu_id_vals.append(df_samples[i].values[j])
                otu_id_list.append(df_samples[i].index[j] - 1)
                otu_dict = {
                    i : otu_id_list,
                    'vals':otu_id_vals                    
                }
                temp_df = pd.DataFrame(data = otu_dict)
                temp_df = temp_df.sort_values(by=['vals'],ascending = False)
        
                otu_and_vals = {
                    'otu_ids':temp_df[i][0:10].tolist(),
                    'sample_values':temp_df['vals'][0:10].tolist()
                }
                final_dict ={i:otu_and_vals}
    sample_vals_list.append(final_dict)