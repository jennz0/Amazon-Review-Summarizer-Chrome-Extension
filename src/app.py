from flask import  request, jsonify, Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

# Get page url from backgound.js
@app.route('/get_url', methods=['POST'])
def get_url():
    data = request.get_json()

    if not request.get_json():
        return jsonify({'status' : "Flask didn't get url"})

    url = request.get_json()['page_url']
    print("Page url:", url)
    print(data)

    # TODO: scape and process the url 

    return jsonify({'status' : "Flask got url"})

if __name__ == "__main__":
    print("*" * 20 + "Starting Flask" + "*"*20)
    app.run(debug=True)