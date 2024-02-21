from flask import Flask, render_template, request
from book_scraper import fetch_book_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        book_title = request.form['book_title']
        description, book_url = fetch_book_info(book_title)
        if description:
            return render_template('result.html', description=description, book_url=book_url)
        else:
            return render_template('result.html', error="Sorry, I couldn't find a description for that book.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
