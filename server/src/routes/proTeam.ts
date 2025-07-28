import { app } from "../entry";
import express, { Express } from 'express';

export const proTeamRouter = express.Router();

// GET /users
proTeamRouter.get('/', (req, res) => {
  res.json([{ id: 1, name: 'Alice' }]);
});

// POST /users
proTeamRouter.post('/', (req, res) => {
  const newUser = req.body;
  res.status(201).json(newUser);
});

