import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}
response = requests.get(url, headers=headers)
response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

data = response.json()
print(data)

import requests
import time

base_item_url = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
story_details = []
headers = {"User-Agent": "TrendPulse/1.0"}

print(f"Fetching details for {len(first_500_items)} stories...")

for i, item_id in enumerate(first_500_items):
    if i % 50 == 0: # Print progress every 50 items
        print(f"  Fetching item {i+1}/{len(first_500_items)} (ID: {item_id})")

    item_url = base_item_url.format(id=item_id)
    try:
        response = requests.get(item_url, headers=headers)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        story_details.append(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching item {item_id}: {e}")

first_500_items = data[:500]
print(f"Number of items fetched: {len(first_500_items)}")
print(first_500_items)

# Add a small delay to avoid hitting API rate limits
    time.sleep(0.05) # 50 milliseconds delay

print(f"Successfully fetched details for {len(story_details)} stories.")
# Display the first 5 story details to verify
print("\nFirst 5 story details:")
for i, story in enumerate(story_details[:5]):
    print(f"Story {i+1}: {story.get('title', 'No Title')} (ID: {story.get('id', 'N/A')})")
    print(f"  URL: {story.get('url', 'N/A')}")

from datetime import datetime

# Create a new DataFrame with the selected fields, starting from stories_df
extracted_stories_df = stories_df.copy()
extracted_stories_df = extracted_stories_df.rename(columns={
    'id': 'post_id',
    'descendants': 'num_comments',
    'by': 'author'
})

# Add the 'collected_at' field with the current date and time
extracted_stories_df['collected_at'] = datetime.now()

# Add a placeholder for the 'category' field
extracted_stories_df['category'] = 'Uncategorized' # Placeholder, will be updated by assign_category

# Select only the desired columns in the specified order
extracted_stories_df = extracted_stories_df[[
    'post_id',
    'title',
    'category',
    'score',
    'num_comments',
    'author',
    'collected_at'
]]

def assign_category(title):
    category_keywords = {
        'technology': ['AI', 'software', 'tech', 'code', 'computer', 'data', 'cloud', 'API', 'GPU', 'LLM'],
        'worldnews': ['war', 'government', 'country', 'president', 'election', 'climate', 'attack', 'global'],
        'sports': ['NFL', 'NBA', 'FIFA', 'sport', 'game', 'team', 'player', 'league', 'championship'],
        'science': ['research', 'study', 'space', 'physics', 'biology', 'discovery', 'NASA', 'genome'],
        'entertainment': ['movie', 'film', 'music', 'Netflix', 'game', 'book', 'show', 'award', 'streaming']
    }

    title_lower = str(title).lower()

    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return category
    return 'General'

extracted_stories_df['category'] = extracted_stories_df['title'].apply(assign_category)
display(extracted_stories_df.head())

import time

# Initialize an empty list to store the selected stories
selected_stories_list = []

# Get all unique categories
all_categories = extracted_stories_df['category'].unique()

print(f"Attempting to collect 25 stories for each of {len(all_categories)} categories...")

for category in all_categories:
    print(f"Processing category: '{category}'...")
    # Select up to 25 stories for the current category
    category_stories = extracted_stories_df[extracted_stories_df['category'] == category].head(25)
    selected_stories_list.append(category_stories)

    # Add a 2-second delay between processing categories
    time.sleep(2)

# Concatenate all selected stories into a single DataFrame
final_stories_df = pd.concat(selected_stories_list)

print(f"Collected a total of {len(final_stories_df)} stories across all categories.")
display(final_stories_df.head())


    print(f"Directory '{output_dir}' already exists.")display(extracted_stories_df.head())
