import pandas as pd
import numpy as np
import csv

df_samples = pd.read_csv("belly_button_biodiversity_samples.csv")
df_otu_id = pd.read_csv("belly_button_biodiversity_otu_id.csv")
df_met_csv  = pd.read_csv("Belly_Button_Biodiversity_Metadata.csv")
df_met  = pd.read_csv("metadata_columns.csv")
df_met_csv_2 = df_met_csv.set_index(df_met_csv['SAMPLEID'])

#List of Names
id_list = df_samples.columns[1:].tolist()

#List of OTU Descriptions
otu_descr = df_otu_id['lowest_taxonomic_unit_found'].tolist()

list_of_dicts_metadata = [df_met_csv_2.loc[x].to_dict() for x in df_met_csv_2['SAMPLEID'].tolist()]

metadata_samples = []
for i in list_of_dicts_metadata:
    filtered_dict = {k:v for (k,v) in i.items()
                       if ('AGE' in k) or ('BBTYPE' in k)
                       or('ETHNICITY' in k) or ('GENDER' in k)
                       or('LOCATION' in k) or ('SAMPLEID' in k)} 
    metadata_samples.append(filtered_dict)

for i in metadata_samples:
    i['AGE'] = i['AGE'].item()
    i['SAMPLEID'] = i['SAMPLEID'].item()
    


