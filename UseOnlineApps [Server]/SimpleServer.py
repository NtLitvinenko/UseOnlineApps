import flask

main = flask.Flask("aaa")

@main.route("/getApp")
def get():
    ah = open("AppCode.app","r").read() #read code for AppCode.app and send to client
    return ah

main.run(port=41)
