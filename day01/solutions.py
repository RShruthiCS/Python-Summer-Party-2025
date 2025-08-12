# Day 1 - WhatsApp Group Analysis

# Q1: Maximum number of participants in October 2024
print((dim_groups[
       (dim_groups['created_date'].dt.month == 10) & 
       (dim_groups['created_date'].dt.year == 2024)]).max())

# Q2: Average number of participants in October 2024
print((dim_groups[
       (dim_groups['created_date'].dt.month == 10) & 
       (dim_groups['created_date'].dt.year == 2024)]['participant_count']).mean())

# Q3: Avg. messages for groups with > 50 participants created in Oct 2024
oct24 = dim_groups[
    (dim_groups['created_date'].dt.month == 10) & 
    (dim_groups['created_date'].dt.year == 2024)]
print(oct24[oct24['participant_count']>50]['total_messages'].mean())
