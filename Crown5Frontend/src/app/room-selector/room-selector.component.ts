import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Player } from '../entities/player';
import { GameStateManagementService } from '../game-state-management.service';
import { WebsocketService } from '../services/websocket.service';

@Component({
  selector: 'app-room-selector',
  templateUrl: './room-selector.component.html',
  styleUrls: ['./room-selector.component.less']
})
export class RoomSelectorComponent {
  public roomNumber: number | null;
  public playerName: string;
  private websocketSub: Subscription;

  constructor(private _websocketService: WebsocketService,
    private _router: Router,
    private _gameStateManagementService: GameStateManagementService,
  ) { }

  joinRoom() {
    let p = new Player();
    p.name = this.playerName;
    this._gameStateManagementService.PlayerInfo = p;

    this._router.navigate(['game', this.roomNumber]);
  }
}
