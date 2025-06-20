import pandas as pd
import numpy as np
from datetime import datetime
import os

# Create the data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate apps.csv
print("Generating apps.csv...")

# App categories
categories = [
    'GAME', 'FAMILY', 'PHOTOGRAPHY', 'MEDICAL', 'TOOLS', 'FINANCE',
    'LIFESTYLE', 'BUSINESS', 'PERSONALIZATION', 'PRODUCTIVITY', 'SPORTS',
    'COMMUNICATION', 'SOCIAL', 'TRAVEL_AND_LOCAL', 'ENTERTAINMENT', 'NEWS_AND_MAGAZINES',
    'DATING', 'EDUCATION', 'HEALTH_AND_FITNESS', 'SHOPPING'
]

# App names (generate 200 unique app names)
adjectives = ['Super', 'Amazing', 'Fantastic', 'Awesome', 'Cool', 'Magic', 'Easy', 'Smart', 
              'Quick', 'Simple', 'Best', 'Pro', 'Ultimate', 'Premium', 'HD', 'Perfect']
nouns = ['Calculator', 'Messenger', 'Tracker', 'Editor', 'Player', 'Camera', 'Browser', 
         'Manager', 'Planner', 'Cleaner', 'Scanner', 'Monitor', 'Recorder', 'Wallet', 
         'Converter', 'Translator', 'Assistant', 'Analyzer', 'Compass', 'Notes']

# Generate 500 app names by combining adjectives and nouns
app_names = []
for i in range(500):
    adj = adjectives[np.random.randint(0, len(adjectives))]
    noun = nouns[np.random.randint(0, len(nouns))]
    app_names.append(f"{adj} {noun} {np.random.randint(1, 10)}")

# Create data for apps
n_apps = 500
apps_data = {
    'App': app_names[:n_apps],
    'Category': np.random.choice(categories, n_apps),
    'Rating': np.random.uniform(1, 5, n_apps).round(1),
    'Reviews': np.random.randint(10, 1000000, n_apps),
    'Size': [f"{np.random.randint(1, 100)}M" for _ in range(n_apps)],
    'Installs': [f"{10**np.random.randint(3, 9)}+" for _ in range(n_apps)],
    'Type': np.random.choice(['Free', 'Paid'], n_apps, p=[0.7, 0.3]),
    'Price': [0 if t == 'Free' else np.random.choice([0.99, 1.99, 2.99, 4.99, 9.99, 19.99, 29.99, 49.99], 1)[0] for t in np.random.choice(['Free', 'Paid'], n_apps, p=[0.7, 0.3])],
    'Content Rating': np.random.choice(['Everyone', 'Teen', 'Mature 17+', 'Adults only 18+', 'Everyone 10+'], n_apps),
    'Genres': np.random.choice(['Action', 'Adventure', 'Arcade', 'Board', 'Card', 'Casino', 'Casual', 'Educational', 'Puzzle', 'Racing', 'Role Playing', 'Simulation', 'Sports', 'Strategy', 'Trivia', 'Word'], n_apps),
    'Last Updated': [datetime.strftime(datetime(2021, np.random.randint(1, 13), np.random.randint(1, 28)), '%B %d, %Y') for _ in range(n_apps)],
    'Current Ver': [f"{np.random.randint(1, 10)}.{np.random.randint(0, 10)}.{np.random.randint(0, 10)}" for _ in range(n_apps)],
    'Android Ver': [f"{np.random.randint(4, 10)}.0 and up" for _ in range(n_apps)]
}

# Convert to DataFrame
apps_df = pd.DataFrame(apps_data)

# 2. Generate user_reviews.csv
print("Generating user_reviews.csv...")

# Generate random reviews for each app
positive_phrases = [
    "Great app! Love it!", 
    "This app is amazing. I use it every day.",
    "Very useful and easy to use.",
    "Best app in this category. Highly recommended!",
    "Excellent features and intuitive interface.",
    "Works perfectly on my device. No issues at all.",
    "I'm very satisfied with this app.",
    "The app is very helpful and well designed.",
    "Amazing performance and great UI.",
    "This app is exactly what I was looking for!"
]

negative_phrases = [
    "This app keeps crashing on my device.",
    "Very disappointing, too many ads.",
    "Needs a lot of improvements.",
    "Waste of money, don't buy it.",
    "The app is very slow and buggy.",
    "I'm having issues with the latest update.",
    "Poor customer support and too expensive.",
    "Not worth the download. Save your time.",
    "Very frustrating experience using this app.",
    "Didn't work as advertised. Uninstalled."
]

neutral_phrases = [
    "The app is okay but could be better.",
    "Average app with basic functionality.",
    "Some features are good, others need work.",
    "It works, but there are better alternatives.",
    "Not bad, but not great either.",
    "It's alright for occasional use.",
    "Decent app but missing some key features.",
    "Works well enough for my needs.",
    "Acceptable performance with some minor issues.",
    "It's just what you'd expect, nothing more."
]

reviews_data = {
    'App': [],
    'Translated_Review': [],
    'Sentiment': [],
    'Sentiment_Polarity': [],
    'Sentiment_Subjectivity': []
}

# Generate reviews
n_reviews_per_app = 10  # Generate 10 reviews per app
for app_name in apps_data['App']:
    for _ in range(n_reviews_per_app):
        sentiment_type = np.random.choice(['Positive', 'Negative', 'Neutral'], p=[0.6, 0.3, 0.1])
        
        if sentiment_type == 'Positive':
            review = np.random.choice(positive_phrases)
            polarity = np.random.uniform(0.5, 1.0)
        elif sentiment_type == 'Negative':
            review = np.random.choice(negative_phrases)
            polarity = np.random.uniform(-1.0, -0.5)
        else:
            review = np.random.choice(neutral_phrases)
            polarity = np.random.uniform(-0.4, 0.4)
            
        subjectivity = np.random.uniform(0.3, 1.0)
        
        reviews_data['App'].append(app_name)
        reviews_data['Translated_Review'].append(review)
        reviews_data['Sentiment'].append(sentiment_type)
        reviews_data['Sentiment_Polarity'].append(round(polarity, 4))
        reviews_data['Sentiment_Subjectivity'].append(round(subjectivity, 4))

# Convert to DataFrame
user_reviews_df = pd.DataFrame(reviews_data)

# Save the DataFrames to CSV
apps_df.to_csv('data/apps.csv', index=False)
user_reviews_df.to_csv('data/user_reviews.csv', index=False)

print("Datasets created successfully!")
print(f"apps.csv: {apps_df.shape[0]} entries")
print(f"user_reviews.csv: {user_reviews_df.shape[0]} entries") 