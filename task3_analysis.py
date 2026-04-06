import pandas as pd

stories_df = pd.DataFrame(story_details)
display(stories_df.head())

from datetime import datetime

# Create a new DataFrame with the selected fields
extracted_stories_df = stories_df.copy()
extracted_stories_df = extracted_stories_df.rename(columns={
    'id': 'post_id',
    'descendants': 'num_comments',
    'by': 'author'
})

# Add the 'collected_at' field with the current date and time
extracted_stories_df['collected_at'] = datetime.now()

# Add a placeholder for the 'category' field
extracted_stories_df['category'] = 'Uncategorized' # Placeholder, needs user-defined logic

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

# Display the first few rows of the new DataFrame
display(extracted_stories_df.head())

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
display(extracted_stories_df.head())
