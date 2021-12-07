from flask import  request, jsonify, Flask
from flask_cors import CORS
from scraper import scrape_reviews as scraper 

app = Flask(__name__)
cors = CORS(app)

# Get page url from backgound.js
@app.route('/get_url', methods=['POST'])
def get_url():
    data = request.get_json()

    if not data:
        return jsonify({'success' : False, 'status' : "Flask didn't get the url."})

    url = data['page_url']
    print("The received url is", url)
    if "amazon" not in url:
        return jsonify({'success' : False, 'status' : "The url is not an amazon product page."})

    reviews = scraper([url])
    print(reviews)
    # TODO:  process the reviews 
    
    return jsonify({'success' : True, 'status' : "Flask got the url."})

if __name__ == "__main__":
    print("*" * 20 + "Starting Flask" + "*"*20)
    app.run(debug=True)