import os
import requests

directory = 'feedback'
txt_files = os.listdir(directory)

list_of_reviews = []
list_of_reviews_dict = []


def process_txt_files():
    for file in txt_files:
        full_path = os.path.abspath(directory + '/' + file)
        with open(full_path, 'r') as review:
            single_review_contents = []
            for line in review.readlines():
                single_review_contents.append(line.strip())
        list_of_reviews.append(single_review_contents)
            

def generate_dictionaries():
    for review in list_of_reviews:
        review_dict = {}
        review_dict['title'] = review[0]
        review_dict['name'] = review[1]
        review_dict['date'] = review[2]
        review_dict['feedback'] = review[3]
        list_of_reviews_dict.append(review_dict)
        
        
def post_to_web_service():
    url = 'web-service-url-here'
    for review in list_of_reviews_dict:
        r = requests.post(url, data=review)
        r.raise_for_status()
        
        
process_txt_files()
generate_dictionaries()
post_to_web_service()