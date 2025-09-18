import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset from GitHub Gist (sample data)
url = 'https://gist.githubusercontent.com/rajkumarboddapati2/022da822d54e968e3f3fcb0f9a8f7a6a/raw/accidentdataset.csv'
df = pd.read_csv(url)

# 2. Display basic info
print(" Dataset Loaded — Shape:", df.shape)
print("\n Sample Records:\n", df.head())

# 3. Parse date and time
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.hour

# Drop any rows where time parsing failed
df.dropna(subset=['Hour'], inplace=True)

# 4. Accidents by Hour of Day
plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title(' Accidents by Hour of the Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

# 5. Accidents by Type
if 'Accident_Type' in df.columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(y='Accident_Type', data=df,
                  order=df['Accident_Type'].value_counts().index,
                  palette='magma')
    plt.title(' Accident Types')
    plt.xlabel('Count')
    plt.ylabel('Type')
    plt.tight_layout()
    plt.show()
else:
    print(" 'Accident_Type' column not found in dataset.")

# 6. Accidents by State (if available)
if 'State' in df.columns:
    plt.figure(figsize=(10, 5))
    top_states = df['State'].value_counts().nlargest(10)
    sns.barplot(x=top_states.index, y=top_states.values, palette='coolwarm')
    plt.title(' Top 10 States with Most Accidents')
    plt.xlabel('State')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.show()

# 7. (Optional) Show missing data stats
missing = df.isnull().sum()
print("\n Missing Values Summary:\n", missing[missing > 0])
