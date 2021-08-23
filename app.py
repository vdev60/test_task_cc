from flask import Flask, request
from flask import render_template
from flask_graphql import GraphQLView
from api.schema import schema
import requests
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_user_data():
    if request.method == "POST":
        username = request.form.get("username")
        response = requests.get(
            f"https://api.github.com/users/{username}")
        if response:
            data = requests.get(
                f"https://api.github.com/users/{username}/repos")
            repos = [i["html_url"] for i in data.json()]
            with open("api/data.json", "w") as f:
                data_set = {"user": username, "repos": repos}
                json.dump(data_set, fp=f, indent=4)
            return render_template(
                "list_repos.html",
                repos=repos,
                username=username)
        else:
            return "<h1>User not found</h1>"

    return render_template("form.html")


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run()
