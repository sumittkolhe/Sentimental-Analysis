@echo off
echo ======================================================
echo Sentiment Analysis for App Reviews - Enhanced Edition
echo ======================================================
echo.
echo This tool analyzes app reviews using:
echo  - Natural Language Processing (NLP)
echo  - Machine Learning classification
echo  - Advanced data visualization
echo  - 1-10 Rating Scale with visual gauge
echo.
echo Features:
echo  - Categorize reviews (Positive/Negative/Neutral)
echo  - Rate reviews on a numerical 1-10 scale
echo  - Visualize sentiment distribution
echo  - Analyze key terms in different sentiment categories
echo  - Interactive prediction tool
echo.

echo Installing required dependencies...
python fix_notebook_dependencies.py
echo.

echo Loading Jupyter Notebook...
echo.

cd /d "%~dp0"
start jupyter notebook "sentiment_analysis_project_compact.ipynb"

echo.
echo If Jupyter doesn't open automatically, please:
echo 1. Open a command prompt
echo 2. Navigate to this directory
echo 3. Run: python fix_notebook_dependencies.py
echo 4. Then run: jupyter notebook sentiment_analysis_project_compact.ipynb
echo.
pause 