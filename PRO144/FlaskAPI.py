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
