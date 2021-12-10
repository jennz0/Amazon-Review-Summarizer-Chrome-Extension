from scraper import *
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize, word_tokenize, PorterStemmer
import math


heaterurl = 'https://www.amazon.com/Kismile-Portable-Electric-Thermostat-Protection/dp/B095NPTQC8/ref=sr_1_3_sspa?gclid=Cj0KCQjwk8b7BRCaARIsAARRTL4ldu37mPv5eV0S1z3zxK2n5plDVY3FgysldvwgSj44NrX9vMVDDW0aAoyNEALw_wcB&hvadid=323598651517&hvdev=c&hvlocphy=9022185&hvnetw=g&hvqmt=b&hvrand=1532303895076506454&hvtargid=kwd-358229541118&hydadcr=29439_10729874&keywords=electric+fan+space+heater&qid=1638739468&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVkdNT1YyUDdLWVg5JmVuY3J5cHRlZElkPUEwMjAzNDc5MzM4RElWVEJJRE1KRiZlbmNyeXB0ZWRBZElkPUEwMzQ1ODUwM0lSN1NONlI5UkNQSSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
vacuumurl = 'https://www.amazon.com/gp/product/B07RHZ6CVX/ref=crt_ewc_img_dp_1?ie=UTF8&psc=1&smid=A1KWJVS57NX03I'
coffeeurl = 'https://www.amazon.com/Breville-Nespresso-USA-BNV550GRY1BUC1-Aeroccino3-Aeroccino/dp/B085SBTSBD?ref_=Oct_DLandingS_D_09dd5360_61&smid=ATVPDKIKX0DER&th=1'
product_links = [vacuumurl]
#Scrape homepages of all urls
review_urls, reviews = [],[]
tot_urls = len(product_links)
for i,link in enumerate(product_links):
    if i > 6:
        break
    print ('-'*20,'Scraping Reviews {}/{}'.format(i+1,tot_urls),'-'*20)
    review_url,review = scrape_product_page(link,driver)
    if review.strip()!= '' and review_url.strip()!='':
        review_urls.append(review_url.strip())
        reviews.append(review)
driver.close()

undesired = []
start_pattern = r'(Reviews with images(.*?)Verified Purchase)'
pattern1 = r'(Reviewed in(.*?)Verified Purchase)'
pattern2 = r'(Read more (.*?)out of 5 stars)'
end_pattern = r'Read more (.*?)all reviews'
end_pattern2 = r'people found(.*?)all reviews'
scraped_review = reviews[0]
scraped_review = re.sub(start_pattern, ' ', scraped_review)
while re.findall(r'Verified Purchase',scraped_review):
    scraped_review = re.sub(pattern1, ' ', scraped_review)
while re.findall(pattern2,scraped_review):
    scraped_review = re.sub(pattern2, ' ', scraped_review)
scraped_review = re.sub(end_pattern, ' ', scraped_review)
scraped_review = re.sub(end_pattern2, ' ', scraped_review)
scraped_review = scraped_review.replace("Your browser does not support HTML5 video.",'')
scraped_review = scraped_review.replace("Video Player is loading.",'')


tokenizer = nltk.RegexpTokenizer(r"\w+")
stop_words = set(stopwords.words('english'))
word_tokens = tokenizer.tokenize(scraped_review)
filtered_tokens = [w for w in word_tokens if not w.lower() in stop_words]

sentences = sent_tokenize(scraped_review) # NLTK function
total_documents = len(sentences)
# print(scraped_review)
def _create_frequency_matrix(sentences):
    frequency_matrix = {}
    stopWords = set(stopwords.words("english"))
    ps = PorterStemmer()

    for sent in sentences:
        freq_table = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            word = ps.stem(word)
            if word in stopWords:
                continue

            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        frequency_matrix[sent[:15]] = freq_table

    return frequency_matrix

def _create_tf_matrix(freq_matrix):
    tf_matrix = {}

    for sent, f_table in freq_matrix.items():
        tf_table = {}

        count_words_in_sentence = len(f_table)
        for word, count in f_table.items():
            tf_table[word] = count / count_words_in_sentence

        tf_matrix[sent] = tf_table

    return tf_matrix

def _create_documents_per_words(freq_matrix):
    word_per_doc_table = {}

    for sent, f_table in freq_matrix.items():
        for word, count in f_table.items():
            if word in word_per_doc_table:
                word_per_doc_table[word] += 1
            else:
                word_per_doc_table[word] = 1

    return word_per_doc_table


def _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents):
    idf_matrix = {}

    for sent, f_table in freq_matrix.items():
        idf_table = {}

        for word in f_table.keys():
            idf_table[word] = math.log10(total_documents / float(count_doc_per_words[word]))

        idf_matrix[sent] = idf_table

    return idf_matrix

def _create_tf_idf_matrix(tf_matrix, idf_matrix):
    tf_idf_matrix = {}

    for (sent1, f_table1), (sent2, f_table2) in zip(tf_matrix.items(), idf_matrix.items()):

        tf_idf_table = {}

        for (word1, value1), (word2, value2) in zip(f_table1.items(),
                                                    f_table2.items()):  # here, keys are the same in both the table
            tf_idf_table[word1] = float(value1 * value2)

        tf_idf_matrix[sent1] = tf_idf_table

    return tf_idf_matrix


def _score_sentences(tf_idf_matrix) -> dict:
    """
    score a sentence by its word's TF
    Basic algorithm: adding the TF frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = {}

    for sent, f_table in tf_idf_matrix.items():
        # print(sent)
        # print(f_table)
        total_score_per_sentence = 0

        count_words_in_sentence = len(f_table)
        for word, score in f_table.items():
            total_score_per_sentence += score

        sentenceValue[sent] = total_score_per_sentence / count_words_in_sentence

    return sentenceValue


def _find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original summary_text
    average = (sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:15] in sentenceValue and sentenceValue[sentence[:15]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary

freq_matrix = _create_frequency_matrix(sentences)
#print(freq_matrix)

'''
Term frequency (TF) is how often a word appears in a document, divided by how many words are there in a document.
'''
# 3 Calculate TermFrequency and generate a matrix
tf_matrix = _create_tf_matrix(freq_matrix)
#print(tf_matrix)

# 4 creating table for documents per words
count_doc_per_words = _create_documents_per_words(freq_matrix)
#print(count_doc_per_words)

'''
Inverse document frequency (IDF) is how unique or rare a word is.
'''
# 5 Calculate IDF and generate a matrix
idf_matrix = _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)
#print(idf_matrix)

# 6 Calculate TF-IDF and generate a matrix
tf_idf_matrix = _create_tf_idf_matrix(tf_matrix, idf_matrix)
#print(tf_idf_matrix)

# 7 Important Algorithm: score the sentences
sentence_scores = _score_sentences(tf_idf_matrix)
#print(sentence_scores)

# 8 Find the threshold
threshold = _find_average_score(sentence_scores)
#print(threshold)

# 9 Important Algorithm: Generate the summary
summary = _generate_summary(sentences, sentence_scores, 0.8* threshold)
print(summary)