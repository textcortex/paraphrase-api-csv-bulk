import csv
import requests

# Don't forget to enter your API key below
TEXTCORTEX_API_KEY = 'YOUR_API_KEY'
TEXTCORTEX_PARAPHRASER_ENDPOINT = "https://api.textcortex.com/v1/texts/paraphrases"
API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TEXTCORTEX_API_KEY}"
}
CSV_FILE = 'food_reviews.csv'


def read_csv():
    """
    This function reads food_reviews.csv and returns the column of "Text" as a list
    here is the column names: Id;ProductId;UserId;ProfileName;HelpfulnessNumerator;HelpfulnessDenominator;Score;Time;Summary;Text

    :return:
    """
    with open(CSV_FILE, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            text_column = [row[9] for row in reader]
        print(text_column)
    return text_column


def generate_paraphrases(list_of_reviews):
    """
    This function generates paraphrases for the "text" column using TextCortex API.
    It then writes the paraphrases to a CSV file with the name "paraphrased_reviews.csv" into paraphrased_text folder
    :param list_of_reviews:
    :return:
    """
    file_name = 'paraphrased_reviews.csv'
    for original_review in list_of_reviews:
        payload = {
            "max_tokens": 64,
            "model": "sophos-1",
            "n": 1,
            "temperature": 0.8,
            "text": original_review
        }
        paraphrased_text = requests.request("POST", TEXTCORTEX_PARAPHRASER_ENDPOINT, json=payload, headers=API_HEADERS)
        if paraphrased_text.status_code == 200:
            with open(file_name, 'a') as f:
                print("Paraphrased text: ", paraphrased_text.json()['data']['outputs'][0]['text'])
                f.write(paraphrased_text.json()['data']['outputs'][0]['text']
                        + ';' + original_review + '\n')
        else:
            print("An error happened while paraphrasing your text. Try again", paraphrased_text.text)


if __name__ == '__main__':
    text_column = read_csv()
    generate_paraphrases(text_column)
