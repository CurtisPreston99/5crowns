import { CardSuit } from "./card-suite.enum";

export class Card {
    constructor(_cardValue: number, _suit: CardSuit) {
        this.cardValue = _cardValue;
        this.suit = _suit;
    }
    public cardValue: number;

    public suit: CardSuit;
}