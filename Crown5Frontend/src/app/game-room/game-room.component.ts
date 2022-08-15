import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Card } from '../common/entities/card';
import { Player } from '../entities/player';
import { GameStateManagementService } from '../game-state-management.service';

@Component({
  selector: 'app-game-room',
  templateUrl: './game-room.component.html',
  styleUrls: ['./game-room.component.less']
})
export class GameRoomComponent implements OnInit {

  public roomId: number;

  public get Players(): Player[] {
    return this._gameStateManagementService.Players;
  }

  
  // public get Board(): Player[] {
  // }

  public get TopOfDiscard(): Card {
    return this._gameStateManagementService.Board.discard[0];
  }


  constructor(private _route: ActivatedRoute, private _gameStateManagementService: GameStateManagementService) { }

  ngOnInit(): void {
    let id = this._route.snapshot.paramMap.get('id');
    if (id) {
      this.roomId = parseInt(id);
      console.log(this.roomId)
      this._gameStateManagementService.joinRoom(this.roomId);
    }
  }

  public startGame() {
    this._gameStateManagementService.startGame();
  }

  public takeFromDiscard() {
    this._gameStateManagementService.takeFromDiscard();
  }
  
  public takeFromDeck() {
    this._gameStateManagementService.takeFromDeck();
  }

}
