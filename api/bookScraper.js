

const fetch = require('node-fetch');
const { URLSearchParams } = require('url');
const { json } = require('micro');

async function fetchBookInfo(bookTitle) {
  const searchParams = new URLSearchParams();
  searchParams.append('book_title', bookTitle);

  const response = await fetch(`http://your-flask-backend-url/book_info?${searchParams.toString()}`);
  const data = await response.json();

  return data;
}

module.exports = async (req, res) => {
  if (req.method === 'GET') {
    const { book_title } = req.query;
    const bookInfo = await fetchBookInfo(book_title);
    res.json(bookInfo);
  } else {
    res.statusCode = 405;
    res.end();
  }
};
