from flask import Flask, request, render_template, redirect, url_for
from google.cloud import bigquery


app = Flask(__name__)
# bigquery_client = bigquery.Client()


@app.route("/")
def main():

    id = request.args.get('id')
    message = request.args.get('message')

    return redirect(
        url_for(
            "get_lists",
            id=id,
            message=message
        )
    )


@app.route("/list")
def get_lists():
    id = request.args.get("id")
    message = request.args.get("message")


    return render_template("list.html", id=id, message=message)


if __name__ == "__main__":
    # ローカルで動かすときに使用
    app.run(host="127.0.0.1", port=8080, debug=True)