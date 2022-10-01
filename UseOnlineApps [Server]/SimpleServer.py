import flask

main = flask.Flask("aaa")

@main.route("/getApp")
def get():
    ah = open("AppCode.app","r").read()
    return ah

main.run(port=41)
