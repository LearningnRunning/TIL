import pandas as pd
from glob import glob
from fuzzywuzzy import fuzz
from tqdm import tqdm

data_path = './data/*.csv'
data_lst = glob(data_path)
amazon_df = pd.read_csv(data_lst[0]).iloc[:,1:]
checco_df_clean = pd.read_csv(data_lst[2])
matching_version = 'brand'

df1 = amazon_df
df2 = checco_df_clean
# Assuming you have loaded the datasets into two DataFrames: df1 and df2

for index, row1 in tqdm(df1.iterrows()):
    product_name1 = row1['brand']
    if type(product_name1) == float:
        continue
    for index, row2 in df2.iterrows():
        product_name2 = row2['brand']

        if type(product_name2) == float:
            continue
        similarity_score = fuzz.ratio(product_name1, product_name2)

        # Set a threshold value for similarity score above which two product names are considered a match
        if similarity_score > 50:  # Adjust the threshold as per your requirement
            # Update the product name in df1 with the matched product name from df2
            df1.at[index, 'checco_brand'] = product_name2
            df1.at[index, 'similarity_score'] = similarity_score
            
            print("product_name1", product_name1)
            print("product_name2", product_name2)
            print("similarity_score", similarity_score)
            break
df1.to_csv(f'fuzzywuzzy_{matching_version}.csv', index=False, encoding='utf-8-sig')