import os

# Define the directory path
output_dir = 'data/'

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created.")
else:
    print(f"Directory '{output_dir}' already exists.")

# Define the output file path for JSON
output_file_json = os.path.join(output_dir, 'trends_20240115.json')

# Save the final_stories_df to a JSON file
final_stories_df.to_json(output_file_json, orient='records', indent=4)

print(f"All stories saved to '{output_file_json}'.")

# Define the output file path
output_file = os.path.join(output_dir, 'trends.csv')

# Save the final_stories_df to a CSV file
final_stories_df.to_csv(output_file, index=False)

print(f"All stories saved to '{output_file}'.")
