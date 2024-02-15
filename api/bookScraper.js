// api/fetchBookInfo.js

const fetch = require("node-fetch");

async function fetchBookInfo(bookTitle) {
  const searchUrl = `https://www.goodreads.com/search?q=${bookTitle.replace(
    " ",
    "+"
  )}`;
  const response = await fetch(searchUrl);
  const body = await response.text();

  // Parsing the HTML response to extract book URL and description
  const descriptionMatch = body.match(
    /<div data-testid="description">(.*?)<\/div>/s
  );
  const bookUrlMatch = body.match(/<a class="bookTitle" href="(.*?)"/);

  const description = descriptionMatch ? descriptionMatch[1].trim() : "";
  const bookUrl = bookUrlMatch ? bookUrlMatch[1] : "";

  return { description, bookUrl };
}

module.exports = async (req, res) => {
  if (req.method === "POST") {
    const { bookTitle } = req.body;

    try {
      const { description, bookUrl } = await fetchBookInfo(bookTitle);
      res.json({ description, bookUrl });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: "Internal Server Error" });
    }
  } else {
    res.status(405).end();
  }
};
