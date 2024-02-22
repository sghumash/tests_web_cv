from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "title": "Sample Jinja Template",
        "header_title": "Welcome to my website",
        "main_title": "About",
        "main_content": "This is some sample content about the website.",
        "footer_content": "Copyright © 2024. All rights reserved."
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
