from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello,world! This is a flask application.'
 if _name_ == '__main__':   
                     
app.run(host='0.0.0.0', port=5000)
