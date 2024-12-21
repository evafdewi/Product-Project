#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('1. Data phyton test.csv')


# In[4]:


df


# In[9]:


from datetime import datetime


# In[10]:


df['Id Transaksi'] = df.apply(lambda row: f"OR-{row['Id Transaksi']}-{datetime.now().strftime('%d%m%Y')}", axis=1)


# In[11]:


df


# In[13]:


valid_orders = df[df['Qty'].notna()]  # Data yang valid (qty tidak kosong)
invalid_orders = df[df['Qty'].isna()]  # Data yang tidak valid (qty kosong)


# In[17]:


valid_orders['Price After Diskon'] = valid_orders['Price'] * (1 - valid_orders['Diskon'] / 100)


# In[21]:


df['Price After Diskon'] = df['Price'] * (1 - df['Diskon'] / 100)


# In[22]:


df


# In[23]:


df['Tanggal Order'] = pd.to_datetime(df['Tanggal Order'])


# In[24]:


df['Jam'] = df['Tanggal Order'].dt.hour


# In[31]:


order_per_jam = df.groupby(['Nama Customer', 'Jam']).size().reset_index(name='Jumlah Order Customer per Jam')


# In[32]:


total_pembelian_per_customer = df.groupby('Nama Customer')['Qty'].sum().reset_index(name='Total Pembelian Customer')


# In[33]:


pembelian_per_produk = df.groupby('Nama Product')['Qty'].sum().reset_index(name='Jumlah Pembelian per Produk')


# In[34]:


print("Jumlah Order Customer per Jam")
print(order_per_jam)
print("Total Pembelian Customer")
print(total_pembelian_per_customer)
print("Jumlah Pembelian per Produk")
print(pembelian_per_produk)


# In[35]:


import matplotlib.pyplot as plt


# In[38]:


plt.figure(figsize=(10, 6))
for customer in order_per_jam['Nama Customer'].unique():
    customer_data = order_per_jam[order_per_jam['Nama Customer'] == customer]
    plt.bar(customer_data['Jam'], customer_data['Jumlah Order Customer per Jam'], label=f'Customer {customer}')
plt.title('Jumlah Order per Customer per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Order')
plt.legend()
plt.show()


# In[48]:


plt.figure(figsize=(10, 6))
plt.barh(total_pembelian_per_customer['Nama Customer'], total_pembelian_per_customer['Total Pembelian Customer'], color='skyblue')
plt.title('Total Pembelian per Customer')
plt.xlabel('Total Pembelian Customer')
plt.ylabel('Nama Customer')
plt.show()


# In[40]:


plt.figure(figsize=(8, 8))
plt.pie(pembelian_per_produk['Jumlah Pembelian per Produk'], labels=pembelian_per_produk['Nama Product'], autopct='%1.1f%%', startangle=90)
plt.title('Jumlah Pembelian per Produk')
plt.axis('equal')  # Untuk membuat pie chart menjadi lingkaran
plt.show()


# In[41]:


valid_orders = df[df['Qty'].notna()]  # Data yang valid (qty tidak kosong)
invalid_orders = df[df['Qty'].isna()]  # Data yang tidak valid (qty kosong)


# In[42]:


invalid_orders


# In[44]:


order_per_customer


# In[45]:


total_pembelian_per_customer 


# In[47]:


pembelian_per_produk


# In[ ]:




