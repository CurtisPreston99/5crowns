import { Component, Input, OnInit } from '@angular/core';
import { Card } from '../common/entities/card';
import { displayValue } from '../common/entities/card-display-value';
import { CardSuit, IconMap } from '../common/entities/card-suite.enum';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.less']
})
export class CardComponent {

  public IconMap: Map<CardSuit, string> = IconMap;
  public displayValue: Map<number, string> = displayValue;

  public getIcon(suit: CardSuit) {
    return IconMap.get(suit);
  }

  @Input()
  public card: Card;

}
