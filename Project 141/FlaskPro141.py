# Download the df1 as articles.csv from the Google Colab.
# 2. Move articles.csv to a new directory. Now, create a new virtual environment with
# Python3.8, activate the environment and pip install required modules into it.
# 3. Create a new file main.py. Import Flask, jsonify and request into it from flask.
# 4. Define the Flask App and write the code that runs the app.
# 5. Import articles.csv and read all the data.
# 6. In the articles.csv, add the header id before the first comma in the first line.
# 7. Save the data from articles.csv into a new variable all_articles without the headers.
# Also create 2 empty lists - liked_articles and not_liked_articles.
# 8. Create the first GET request to get the first article. Here, return the first article.
# 9. Create the second POST request to mark the article as liked. Here, add the article into
# the liked_articles and remove the article from all_articles. Return the success
# response.
# 10.Create the third POST request to mark the article as not liked. Here, add the article
# into the not_liked_articles and remove the article from all_articles. Return the success
# response.
# 11.Test the API with Postman to see if everything works fine!

from flask import Flask, jsonify, request
import csv

articles = []
with open('articles.csv') as f:
    r = csv.reader(f)
    data = list(r)
    allArticles = data[1:]

app = Flask(__name__)

likedArticles = []
unlikedArticles = []

@app.route('/articles')
def getArticles():
    return jsonify({
        'data' : allArticles[0],
        'status' : 'success'
    })

@app.route('/liked', methods = ['POST'])
def likedArticles():
    header = articles[0]
    all = articles[1:]
    likedArticles.append(header)
    return jsonify({
            'status' : 'success'
    })  

@app.route('/unliked', methods = ['POST'])
def unlikedArticles():
    header = articles[0]
    all = articles[1:]
    unlikedArticles.append(header)
    return jsonify({
            'status' : 'success'
    })  

if __name__ == '__main__':
    app.run()
