from flask import Flask, jsonify, request
from Storage import liked, unliked, articles
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
def recommendedArticles():
    a = []
    for i in liked:
        output = recommendArticle(int(i['contentId']))
        for data in output:
            a.append(data)
    import itertools
    a.sort()
    a = list(a for a,_ in itertools.groupby(a)) 
    articleData = []
    for r in a:
        d = {
            'title' : r[0],
            'lang' : r[1],
            'contentType' : r[2],
            'eventType': r[3]
        }
    articleData.append(d)
    return jsonify({
        'data' : articleData,
        'status': 'success'
    }), 200
    
@app.route('/liked', methods = ["POST"])
def likedArticles():
    id = request.args.get("id")
    data = next(i for i in articles if i["id"] == id)
    articles.remove(data)
    liked.append(data)
    return jsonify({
        "status": "Success!"
    }), 200

@app.route('/unliked', methods = ["POST"])
def unlikedArticles():
    id = request.args.get("id")
    data = next(i for i in articles if i["id"] == id)
    articles.remove(data)
    unliked.append(data)
    return jsonify({
        "status": "Success!"
    }), 200

@app.route("/popular-articles")
def popular_articles():
    return jsonify({
        "data": output,
        "status": "Success!"
    }), 200


if __name__ == '__main__':
    app.run()

