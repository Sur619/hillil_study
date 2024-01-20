from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    #return 'Hello world!'

    #return hello world in HTML
    #return '<h1>Hello world</h1><p>this is paragrah</p><p>this is another paragrah</p>'


    #return hallo world in HTML with CSS
    #'<h1 style='color:red'>hello wolrd</h1><p>this is paragrah</p><p>this is anither paragrah</p>'
    return {
        'name':'John',
        'age':21,
        'city':'Kyiv'
    }



if __name__ == '__main__':
    app.run(debug=True)