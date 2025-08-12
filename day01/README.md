# Day 01 – WhatsApp Group Analysis

📅 **Challenge Date:** Day 1 of 15  
🔍 **Theme:** WhatsApp group messaging behavior  
📊 **Dataset:** `dim_groups` (pre-loaded DataFrame)

---
You are a Product Analyst on the WhatsApp team investigating group messaging dynamics.
Your team wants to understand how large groups are being used and their messaging
patterns. You'll leverage data to uncover insights about group participation and
communication behaviors.

### 🧩 Question 1
**Prompt:**  
What is the maximum number of participants among WhatsApp groups that were created in October 2024? This metric will help us understand the largest group size available.

**Code:**
```python
print((dim_groups[
    (dim_groups['created_date'].dt.month == 10) & 
    (dim_groups['created_date'].dt.year == 2024)
]['participant_count']).max())
```

---
### 🧩 Question 2
**Prompt:**
What is the average number of participants in WhatsApp groups that were created in October 2024? This number will indicate the typical group size and inform our group messaging feature considerations. 

**Code:**
```python
print((dim_groups[
    (dim_groups['created_date'].dt.month == 10) & 
    (dim_groups['created_date'].dt.year == 2024)
]['participant_count']).mean())
```

---
### 🧩 Question 3
**Prompt**
For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent? This insight will help assess engagement in larger groups and support recommendations for group messaging features.

**Code:**
```python
oct24 = dim_groups[
    (dim_groups['created_date'].dt.month == 10) & 
    (dim_groups['created_date'].dt.year == 2024)
]
print(oct24[oct24['participant_count'] > 50]['total_messages'].mean())
```

---

