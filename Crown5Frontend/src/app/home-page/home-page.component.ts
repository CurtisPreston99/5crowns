import { Component, OnInit } from '@angular/core';
import { from } from 'rxjs';
import { Card } from '../common/entities/card';
import { CardSuit } from '../common/entities/card-suite.enum';

@Component({
    selector: 'app-home-page',
    templateUrl: './home-page.component.html',
    styleUrls: ['./home-page.component.less']
})
export class HomePageComponent {
    public cards: Card[] = [];
    constructor() {
        const suits = Object.keys(CardSuit).filter((v) => isNaN(Number(v)));
        suits.forEach((suit, index) => {
            // 👇️ Small, Medium, Large
            for (let i = 0; i <= 13; i++) {
                this.cards.push(new Card(i, suit as unknown as CardSuit))
            }
            console.log(suit);
        });
        this.cards.push(new Card(50, CardSuit.Clovers))
        console.log(this.cards);
    }
}
