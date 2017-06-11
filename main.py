from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():

    #TODO: activate the following block of code once rPi JSON object can be received
    #reqeust and set json data from rPi
    #wash1status = request.json['w1status']
    #wash2status = request.json['w2status']
    #dry1status = request.json['d1status']
    #dry2status = request.json['d2status']

    #Test wash/dry status on template
    wash1status = 'available'
    wash2status = 'available'
    dry1status = 'available'
    dry2status = 'available'

    #conditional formatting for template found in index.html

    return render_template('index.html', index=index)

if __name__ == "__main__":
    app.run(debug=True)