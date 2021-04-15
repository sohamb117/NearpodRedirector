from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/<link>")
def main(link=""):
	if link!="":
		return redirect((f"https://app.nearpod.com/presentation?pin={link}"))
	else:
		#if(request.args.get("query")==None):
		return render_template("index.html")
		#else:
			#return redirect((f"https://app.nearpod.com/presentation?pin={request.args.get('query')}"))

#@app.route("/")
#def main():
#	return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
