import { CardSuit } from "./card-suite.enum";

export class Card {
    constructor(_cardValue: number, _suit: CardSuit) {
        this.value = _cardValue;
        this.suit = _suit;
    }
    public value: number;

    public suit: CardSuit;
}