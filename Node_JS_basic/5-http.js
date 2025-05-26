const http = require('http');
const countStudents = require('./3-read_file_async');

const DataBase = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const studentList = await countStudents(DataBase);
      res.end(`This is the list of our students\n${studentList}`);
    } catch (err) {
      res.end(`This is the list of our students\n${err.message}`);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;