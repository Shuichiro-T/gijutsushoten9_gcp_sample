from flask import Flask, request, render_template, redirect, url_for
from google.cloud import bigquery


app = Flask(__name__)
bigquery_client = bigquery.Client()


@app.route("/")
def main():
    # リクエストパラメータからIDとMESSAGEを取得
    id = request.args.get('id')
    message = request.args.get('message')

    # データ作成用SQLの構築
    query = 'INSERT INTO DATASET1.TABLE1 (ID, MESSAGE)' \
     + f'VALUES ({id}, \"{message}\" )'

    # SQLの実行
    bigquery_client.query(query).result()

    return redirect(
        url_for(
            "get_lists"
        )
    )

@app.route("/list")
def get_lists():

    # データ取得用のSQL作成
    query = 'SELECT * FROM DATASET1.TABLE1'

    # データの取得
    results = bigquery_client.query(query).result()

    # 取得結果をlist.htmlへ渡す
    return render_template("list.html", results=results)


if __name__ == "__main__":
    # ローカルで動かすときに使用
    app.run(host="127.0.0.1", port=8080, debug=True)