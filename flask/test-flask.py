from flask import Flask

app = Flask(__name__)

ncall=0

@app.route("/")
def hello():
    global ncall
    ncall = ncall +1
    return "Hello World! "+str(ncall)

if __name__ == "__main__":
    app.run()
