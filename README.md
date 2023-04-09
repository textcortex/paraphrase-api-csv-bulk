# Paraphrase CSV files using TextCortex API
Welcome to another episode of TextCortex API How-To's. In this episode, we will show you how to paraphrase CSV files using TextCortex API.

## Prerequisites
- Python 3.6 or higher
- TextCortex API key
- CSV file with a column named "text" containing the text to be paraphrased
- A text editor
- A terminal

## Installation
- Clone this repository
- Install the requirements using `pip install -r requirements.txt`

## Usage
- Open `paraphrase_csv.py` in your favourite code editor. Mine is [PyCharm](https://www.jetbrains.com/pycharm/).
- Replace the `api_key` variable with your API key. If you don't have one, head over to [TextCortex](https://www.textcortex.com/) and sign up for a free account. After signing up, you can find your API key in the settings -> API tab.
- Script will look for a while called food_reviews.csv in the same directory as the script. If you want to use a different file, you can add your own file and then change the name of the file in the `csv_file` variable.

