import { Card } from "./card";

export class Board {
    public deck: Card[];
    public discard: Card[];
    public playerTurn: number;
}