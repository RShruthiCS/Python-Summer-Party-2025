# Day 02 – Amazon Sponsored Ad Analysis

📅 **Challenge Date:** Day 2 of 15  
🏢 **Theme:** Amazon Sponsored Ads CTR Optimization  
📊 **Datasets Used:**  
- `fct_ad_performance` (fact table with ad metrics)  
- `dim_product` (product metadata)

---

### 🧩 Question 1

**Prompt:**  
What is the average click-through rate (CTR) for sponsored product ads for each product category that contains the substring "Electronics" in its name during October 2024?

**Code:**
```python
combined = pd.merge(fct_ad_performance, dim_product, on='product_id')
oct24 = combined[
    (combined['recorded_date'].dt.month == 10) &
    (combined['recorded_date'].dt.year == 2024)
]
final = oct24[oct24['product_category'].str.contains('Electronics')]
final['ctr'] = final['clicks'] / final['impressions']
grouped = final.groupby('product_category')['ctr'].mean()
print(grouped)
```

---
### 🧩 Question 2
**Prompt:**
Which product categories have a CTR greater than the overall average CTR for sponsored product ads during October 2024?

**Code:**
```python
final['category_ctr_mean'] = final.groupby('product_category')['ctr'].transform('mean')
print(final[final['category_ctr_mean'] > final['ctr'].mean()]['product_category'])
```

---
### 🧩 Question 3
**Prompt:**
What is the percentage difference between the category CTRs (from Q2) and the overall average CTR for October 2024?

**Code:**
```python
ctr_more = final[final['category_ctr_mean'] > final['ctr'].mean()][
    ['product_category', 'category_ctr_mean']
].drop_duplicates()

overall_ctr = final['ctr'].mean()
ctr_more['percentage_diff'] = ((ctr_more['category_ctr_mean'] - overall_ctr) / overall_ctr) * 100

print(ctr_more[['product_category', 'percentage_diff']])
```

---

