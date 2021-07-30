
from flask import Flask, jsonify, request
from Storage import liked, notLiked, articles
from Demographic import output
from Content import recommendArticle

app = Flask(__name__)
@app.route('/articles')
def getArticles():
    aData = {
      'title': articles[0][13],
      'eventType' : articles[0][4],
      'contentType' : articles[0][11],
      'lang': articles[0][15]
    }
    return jsonify({
        'data': aData, 
        'status': 'success'
    })


@app.route('/recommend', methods = ['POST'])
def recommendedMovies():
    a = []
    for i in liked:
        output = recommendArticle(i[13])
        for data in output:
            a.append(data)
    import itertools
    a.sort()
    a = list(a for a,_ in itertools.groupby(a)) 
    articleData = []
    for i in a:
        d = {
            'title' : i[0],
            'lang' : i[1],
            'contentType' : i[2],
            'eventType': i[3]
        }
    articleData.append(a)
    return jsonify({
        'data' : articleData,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run()

