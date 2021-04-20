from flask import Flask, render_template
app = Flask(__name__)
posts=[
    {
        'author':'logith',
        'title': 'blog post 1',
        'content':'my first content',
        'date':'april 19 2020'
    },
    {
        'author':'kumar',
        'title': 'blog post 2',
        'content':'my second content',
        'date':'april 20 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)
@app.route('/about')
def about():
    return render_template('about.html',title='About')
        
if __name__=='__main__':
    app.run(debug=True)            