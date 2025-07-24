import express, { Express } from 'express';

const port = 3000;
const app : Express = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  return console.log(`Express is listening at http://localhost:${port}`);
});