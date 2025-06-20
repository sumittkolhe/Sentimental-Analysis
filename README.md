# Sentiment Analysis of App Reviews

##  Project Overview
This project analyzes sentiment in app reviews from Google Play Store to uncover insights about user satisfaction and app performance. Using natural language processing (NLP) and machine learning techniques, the notebook categorizes reviews as positive, negative, or neutral, helping developers understand user feedback and improve their applications.

##  Key Features
- **Sentiment Analysis**: Automatically classifies reviews as positive, negative, or neutral
- **1-10 Rating Scale**: Converts sentiment polarity to an intuitive 1-10 scale
- **Visual Dashboards**: Interactive charts and visualizations of sentiment patterns
- **Word Cloud Analysis**: Visualizes common terms in positive and negative reviews
- **Predictive Modeling**: ML models to predict sentiment of new reviews
- **Interactive Demo**: Test the sentiment analyzer with your own text

##  Technologies Used
- **Python**: Pandas, NumPy for data manipulation
- **Visualization**: Matplotlib, Seaborn, Plotly
- **NLP**: NLTK, TextBlob for text processing
- **Machine Learning**: scikit-learn for classification models
- **Interactive UI**: Jupyter widgets (ipywidgets)

##  Requirements
```
pandas>=1.3.0
numpy>=1.20.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
scikit-learn>=0.24.0
nltk>=3.6.0
textblob>=0.15.3
wordcloud>=1.8.0
jupyter>=1.0.0
ipywidgets>=7.6.0
nbformat>=4.2.0
```

##  Installation & Setup

### Option 1: Using the batch file (Windows)
1. Run the `run_sentiment_analysis.bat` file by double-clicking it
2. This will install all dependencies and open the notebook automatically

### Option 2: Manual setup
1. Install dependencies:
   ```bash
   python fix_notebook_dependencies.py
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook sentiment_analysis_project_compact.ipynb
   ```

##  Project Structure
- `sentiment_analysis_project_compact.ipynb`: Main project notebook
- `play-store-sentiment-analysis-of-user-reviews.ipynb`: Extended version with more analyses
- `fix_notebook_dependencies.py`: Helper script to install required packages
- `run_sentiment_analysis.bat`: Windows batch file to run the project
- `data/`: Directory containing the dataset files
  - `apps.csv`: Information about applications
  - `user_reviews.csv`: User reviews with sentiment labels

##  How to Use the Interactive Analyzer
1. Run all notebook cells
2. Scroll to the "Interactive Sentiment Analyzer" section
3. Enter a review in the text area
4. Select a model from the dropdown
5. Click "Analyze Sentiment" to see:
   - Sentiment classification (positive/negative/neutral)
   - Rating on a 1-10 scale with visual gauge
   - Confidence scores for sentiment predictions

##  Example Reviews to Try
1. "This app is amazing! I love using it every day."
2. "The app keeps crashing on my device. Very frustrating."
3. "It's okay but could use some improvements."

##  Troubleshooting
If you encounter dependency issues:
1. Ensure Python 3.6+ is installed
2. Run `python fix_notebook_dependencies.py`
3. For specific issues with ipywidgets: `pip install ipywidgets`
4. For Plotly display issues: `pip install nbformat>=4.2.0`
5. Restart the Jupyter kernel after installing packages

##  Key Insights
The analysis reveals:
- Most app categories have predominantly positive sentiment
- Free vs. paid apps show distinct sentiment distribution patterns
- Common terms in positive reviews: "great", "love", "easy", "best"
- Common terms in negative reviews: "crash", "bug", "waste", "fix"
- Sentiment often correlates with app ratings and review length

##  Future Enhancements
- Implement more advanced NLP techniques
- Add aspect-based sentiment analysis
- Create a standalone web application
- Support for multiple languages
- Time-series analysis of sentiment trends 