from flask import *
import requests

app = Flask(__name__)

URL = "https://test.devilhai.online/"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/all")
def accounts():
    try:
        response = requests.get(URL + "all_accounts")
        data = response.json()
        return render_template("all_accounts.html", account=data)
    except Exception as e:
        return str(e)


@app.route("/delete")
def delete_account():
    return "I am delete function and call when you clicked on delete"

def 


if __name__ == "__main__":
    app.run(debug=True)
    
    




    



