#!usr/bin/env python
import os
import markdown
from flask import Flask
from flask import abort
from flask import url_for
from flask import render_template
from flask import Markup

app = Flask(__name__)
@app.route('/')
def index():
    try: 
        path = os.path.join('md', 'example.md')
        f = open(path)
        title = 'index'
        content = Markup(markdown.markdown(f.read(), extensions=['gfm']))
        return render_template('index.html', **locals())
    except:
        abort(404)

@app.route('/<filename>/')
def md_file(filename):
    try: 
        path = os.path.join('md', filename + '.md')
        f = open(path)
        title = Markup(filename)
        content = Markup(markdown.markdown(f.read(), extensions=['gfm']))
        return render_template('index.html', **locals())
    except:
        abort(404)

if __name__ == '__main__':
    app.run()
