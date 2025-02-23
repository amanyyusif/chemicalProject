import pandas as pd
import matplotlib.pyplot as plt
import os 

#read data 
my_data = pd.read_csv('C:/Users/HP/chemicalProject/cscpopendata.csv')
my_data.info()

my_data.duplicated().sum()

#duplecates will be removed for this analysis
clean_data = my_data.drop_duplicates().copy()
clean_data.info()

clean_data['BrandName'].isna().sum()

#checking brand names for Merle Norman Cosmetics company we find that it has only one name but with diffrent formats
clean_data[clean_data['CompanyName'] == 'Merle Norman Cosmetics']['BrandName'].unique()

clean_data['BrandName'] = clean_data['BrandName'].fillna('Merle Norman Cosmetics')

clean_data['BrandName'] = clean_data['BrandName'].replace(['Merle Norman', 'Merle Norman ','MERLE NORMAN ','MERLE NORMAN','MERLE NORMAN COSMETICS, INC. '],'Merle Norman Cosmetics')

clean_data[clean_data['CompanyName'] == 'Merle Norman Cosmetics']['BrandName'].unique()

clean_data.info()

clean_data['ChemicalName'].nunique()

chemical_tyeps_count = clean_data['SubCategory'].value_counts()
chemical_tyeps_count.head(30)

chemical_tyeps_count = clean_data['PrimaryCategory'].value_counts()
chemical_tyeps_count

discounted_prime = clean_data.groupby(['PrimaryCategory'])['DiscontinuedDate'].count().sort_values(ascending=False)

discounted_prime_df = pd.DataFrame(discounted_prime)
discounted_prime_df = discounted_prime_df.reset_index()
discounted_prime_df.head(5)

plt.barh(discounted_prime_df.head(5).PrimaryCategory,discounted_prime_df.head(5).DiscontinuedDate)
plt.title("Discontinued products")
plt.ylabel("Prime Category")
plt.xlabel("Discontinued Date")
plt.box(on=False)
#plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)
# plt.show()
plt.savefig("output_plot.png") 


chemicals_per_product_prime = clean_data.groupby(['PrimaryCategory'])['ChemicalName'].value_counts().sort_values(ascending=False)

chemicals_per_product_prime_dt = pd.DataFrame(chemicals_per_product_prime).reset_index()

chemicals_per_product_prime_dt

company_discontinued = clean_data.groupby(['CompanyName'])['DiscontinuedDate'].count().sort_values(ascending=False)

company_discontinued_df = pd.DataFrame(company_discontinued).reset_index()
company_discontinued_df.head(5)
# company_discontinued_df.tail(5)
chemicals_in_makeup = clean_data[clean_data.PrimaryCategory=='Makeup Products (non-permanent)']['ChemicalName'].value_counts()

chemicals_in_makeup_df = pd.DataFrame(chemicals_in_makeup).reset_index()
chemicals_in_makeup_df.head(5)

brands_upper = clean_data['BrandName'].str.strip().str.upper()
all_upper_brands = brands_upper.value_counts().head(10)

brands_df = pd.DataFrame(all_upper_brands).reset_index()
brands_df.head(10)

clean_data.to_csv("Clean_data.csv")

