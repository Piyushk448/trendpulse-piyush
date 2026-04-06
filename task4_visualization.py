print(f"Total stories collected: {len(final_stories_df)}")

# Count the number of stories per category
category_counts = extracted_stories_df['category'].value_counts()
display(category_counts)
