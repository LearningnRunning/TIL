import pandas as pd
from glob import glob
from fuzzywuzzy import fuzz
from tqdm import tqdm

data_path = './data/*.csv'
data_lst = glob(data_path)

# 매핑할 사이트 데이터
amazon_df = pd.read_csv(data_lst[1]).iloc[:,1:]

# 체코 데이터
checco_df_clean = pd.read_csv(data_lst[0])
matching_version = 'brand'

# 컬럼명 맞춰줘야 해요
df1 = amazon_df.drop_duplicates(subset=['brand'])
df2 = checco_df_clean.drop_duplicates(subset=['brand'])
# Assuming you have loaded the datasets into two DataFrames: df1 and df2

for index, row1 in tqdm(df1.iterrows(), total= df1.shape[0]):
    max_score = 70
    # 컬럼명 맞춰줘야 해요
    product_name1 = row1['brand']
    if type(product_name1) == float:
        continue
    for index, row2 in df2.iterrows():
        # 컬럼명 맞춰줘야 해요
        product_name2 = row2['brand']

        if type(product_name2) == float:
            continue
        similarity_score = fuzz.ratio(product_name1, product_name2)

        # Set a threshold value for similarity score above which two product names are considered a match
        if similarity_score >= 90:
            print("product_name1", product_name1)
            print("product_name2", product_name2)
            print("similarity_score", similarity_score)
            break
        elif similarity_score > max_score:  # Adjust the threshold as per your requirement
            max_score = similarity_score
            # Update the product name in df1 with the matched product name from df2
            df1.at[index, 'checco_brand'] = product_name2
            df1.at[index, 'similarity_score'] = similarity_score

df1.to_csv(f'fuzzywuzzy_{matching_version}_drop.csv', index=False, encoding='utf-8-sig')