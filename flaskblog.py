from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Jacob Dumas',
        'title': 'Blog Post 1',
        'content': 'First post comment',
        'date_posted': 'April 30, 2022'
    },
        {
        'author': 'Jacob Dumas',
        'title': 'Blog Post 2',
        'content': 'post comment',
        'date_posted': 'May 15, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)