import { app } from "../entry";
import express, { Express } from 'express';

export const playerRouter = express.Router();

// GET REQUESTS --------------------------------
enum GetRequestsTypes {
  MATCHING_PLAYER = "/matching_player",
}

playerRouter.get(GetRequestsTypes.MATCHING_PLAYER, (req, res) => {
  res.json([{ id: 1, name: 'Alice' }]);
});

playerRouter.get('/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ id: userId, name: 'Alice' });
});



