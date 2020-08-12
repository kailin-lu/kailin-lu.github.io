from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello!'

@app.route('/projects')
def projects():
    return '<h1>Projects</h1>'

@app.route('/posts')
def posts():
    return 'Recent posts'


if __name__=='__main__':
    app.run(debug=True)

