export enum CardSuit {
    Hearts = "Hearts",
    Diamonds = "Diamonds",
    Clovers = "Clovers",
    Spades = "Spades",
    Stars = "Stars"
}


export const IconMap: Map<CardSuit, string> = new Map<CardSuit, string>([
    [CardSuit.Hearts, "./assets/suits/Hearts.png"],
    [CardSuit.Diamonds, "./assets/suits/Diamonds.png"],
    [CardSuit.Clovers, "./assets/suits/Clovers.png"],
    [CardSuit.Spades, "./assets/suits/Spades.png"],
    [CardSuit.Stars, "./assets/suits/Stars.png"],
]);