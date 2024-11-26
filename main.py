from flask import Flask, request

app = Flask(__name__)


# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name"><br>
          一言: <input type="text" comment="comment"><br>
          <input type="submit" value="送信">
        </form>
        </body></html>
    """


# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    comment = request.args.get('comment')
    if name is None: name = 'anonymous'
    if comment is None: comment = 'no comment'
    # 自己紹介を自動作成
    return """
    <h1>{0}さん、こんにちは！</h1>
    <h2>{0}さんは最高ですね！</h2>
    <h3>ひとこと:{1}</h3>
    """.format(name, comment)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
