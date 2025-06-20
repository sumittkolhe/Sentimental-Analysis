#!/usr/bin/env python3
# fix_notebook_dependencies.py - Install requirements for Sentiment Analysis notebook

import subprocess
import sys

def install_package(package):
    """Install a package using pip."""
    print(f"Installing {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to install {package}: {e}")
        return False

def main():
    """Install all required packages for the sentiment analysis notebook."""
    print("Installing dependencies for Sentiment Analysis project...")
    
    # List of required packages with minimum versions
    required_packages = [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "plotly",
        "nltk",
        "scikit-learn",
        "textblob",
        "wordcloud",
        "ipywidgets",
        "nbformat>=4.2.0",  # Fix for Plotly rendering issue
        "jupyter",
        "notebook"
    ]
    
    # Install all packages
    success_count = 0
    for package in required_packages:
        if install_package(package):
            success_count += 1
    
    # Download NLTK resources
    try:
        print("\nDownloading NLTK resources...")
        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        print("✅ NLTK resources downloaded successfully")
    except Exception as e:
        print(f"⚠️ Failed to download NLTK resources: {e}")
    
    # Report summary
    print("\n==========================================")
    print(f"Installed {success_count} of {len(required_packages)} packages")
    print("==========================================")
    
    if success_count == len(required_packages):
        print("\n✅ All packages installed successfully!")
        print("You can now run the notebook with: jupyter notebook sentiment_analysis_project_compact.ipynb")
    else:
        print("\n⚠️ Some packages failed to install. Check the messages above.")
    
    # Add extra help for nbformat issue
    print("\nIf you encounter the error 'Mime type rendering requires nbformat>=4.2.0':")
    print("1. Make sure you've restarted your Jupyter notebook server after running this script")
    print("2. Verify nbformat is installed: pip show nbformat")
    print("3. If problems persist, try: pip install --upgrade nbformat")

if __name__ == "__main__":
    main() 