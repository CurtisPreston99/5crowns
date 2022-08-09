import { Component, OnInit } from '@angular/core';
import { Player } from '../entities/player';
import { GameStateManagementService } from '../game-state-management.service';

@Component({
  selector: 'app-game-room',
  templateUrl: './game-room.component.html',
  styleUrls: ['./game-room.component.less']
})
export class GameRoomComponent implements OnInit {

  public get Players() : Player[] {
    return this._gameStateManagementService.Players;
  }
  

  constructor(private _gameStateManagementService: GameStateManagementService) { }

  ngOnInit(): void {
  }

  public startGame(){
    this._gameStateManagementService.startGame();
  }

}
