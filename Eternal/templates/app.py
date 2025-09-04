from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route('/api/search')
def search():
    query = request.args.get('query')

    # For now, return dummy data
    dummy_data = [
        {
            "title": f"{query.title()} - Sample Product",
            "amazon_price": 12999,
            "flipkart_price": 13499,
            "image": "https://via.placeholder.com/150",
            "link_amazon": "https://amazon.in",
            "link_flipkart": "https://flipkart.com"
        }
    ]
    return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)
