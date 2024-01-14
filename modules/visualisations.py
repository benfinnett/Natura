import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Creating a DataFrame with all the provided data
all_data = {
    'Prompt ID': range(1, 18),
    'Fastest Time (s) ChatGPT': [2.837, 3.124, 3.192, 1.531, 1.852, 1.201, 3.845, 2.462, 2.468, 1.984,
                                6.314, 1.532, 0.917, 3.267, 1.265, 0.892, 1.037],
    'Slowest Time (s) ChatGPT': [3.36, 3.746, 3.928, 2.345, 2.621, 66.426, 3.998, 3.127, 3.011, 2.812,
                                6.937, 2.5, 1.291, 4.116, 1.838, 1.152, 1.344],
    'Average Time (s) ChatGPT': [3.029, 3.489, 3.646, 1.952, 2.241, 14.332, 3.922, 2.874, 2.696, 2.368,
                                6.616, 2.173, 1.071, 3.675, 1.614, 1.034, 1.18],
    'Correct Output ChatGPT': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes',
                             'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes'],
    'Fastest Time (s) Mistral': [85.237, 85.148, 78.804, 53.486, 54.17, 49.155, 94.141, 78.611, 99.784, 65.388,
                                105.324, 51.716, 79.053, 97.136, 89.004, 69.397, 55.994],
    'Slowest Time (s) Mistral': [788.347, 94.184, 90.857, 72.348, 81.956, 59.776, 111.253, 99.981, 115.947, 82.131,
                                111.199, 64.283, 90.001, 131.383, 96.553, 80.112, 73.182],
    'Average Time (s) Mistral': [419.148, 89.993, 86.964, 61.182, 68.054, 52.891, 101.248, 95.417, 106.984, 75.351,
                                108.79, 57.524, 85.511, 116.384, 93.252, 75.963, 62.591],
    'Correct Output Mistral': ['No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No',
                             'No', 'No', 'No', 'No', 'No', 'Yes', 'No']
}

all_df = pd.DataFrame(all_data)

# Convert 'Correct Output' to a boolean
all_df['Correct Output ChatGPT'] = all_df['Correct Output ChatGPT'].map({'Yes': True, 'No': False})
all_df['Correct Output Mistral'] = all_df['Correct Output Mistral'].map({'Yes': True, 'No': False})

# Visualisations
# Bar graph 
plt.figure(figsize=(14, 10))
sns.barplot(x='Prompt ID', y='Average Time (s) Mistral', data=all_df,  label='Mistral')
sns.barplot(x='Prompt ID', y='Average Time (s) ChatGPT', data=all_df,  label='ChatGPT')
plt.title('Comparison of Average Time to Compile per Prompt ID')
plt.legend()
plt.show()

# Line graph
plt.figure(figsize=(14, 10))
plt.plot(all_df['Prompt ID'], all_df['Fastest Time (s) ChatGPT'], marker='x', label='Fastest ChatGPT')
plt.plot(all_df['Prompt ID'], all_df['Slowest Time (s) ChatGPT'], marker='x', label='Slowest ChatGPT')
plt.plot(all_df['Prompt ID'], all_df['Fastest Time (s) Mistral'], marker='o', linestyle='--', label='Fastest Mistral')
plt.plot(all_df['Prompt ID'], all_df['Slowest Time (s) Mistral'], marker='o', linestyle='--', label='Slowest Mistral')
plt.xlabel('Prompt ID')
plt.ylabel('Time (s)')
plt.title('Fastest and Slowest Times per Prompt ID')
plt.legend()
plt.show()

# Pie chart
colors = ["#1F77B4", "#FF7F0E"]
correct_counts_set1 = all_df['Correct Output ChatGPT'].value_counts()
correct_counts_set2 = all_df['Correct Output Mistral'].value_counts()

plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.pie(correct_counts_set1, labels=correct_counts_set1.index, autopct='%1.1f%%', startangle=140, colors=colors) # type: ignore
plt.title('ChatGPT Proportion of Correct Outputs')

plt.subplot(1, 2, 2)
plt.pie(correct_counts_set2, labels=correct_counts_set2.index, autopct='%1.1f%%', startangle=140, colors=colors[::-1]) # type: ignore
plt.title('Mistral Proportion of Correct Outputs')
plt.show()

