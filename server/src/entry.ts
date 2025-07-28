import express, { Express } from 'express';
import { playerRouter } from './routes/players';
import { proTeamRouter } from './routes/proTeam';
import cors from 'cors';

const port : number = 3000;
export const app : Express = express();

app.use(cors());

// parse JSON  bodies
app.use(express.json());

// add routes for specifc types of request
app.use('/player', playerRouter);
app.use('/proTeam', proTeamRouter);

app.listen(port, () => {
  return console.log(`Express is listening at http://localhost:${port}`);
});