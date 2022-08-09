import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { WebsocketService } from '../services/websocket.service';

@Component({
  selector: 'app-room-selector',
  templateUrl: './room-selector.component.html',
  styleUrls: ['./room-selector.component.less']
})
export class RoomSelectorComponent implements OnDestroy {
  public roomNumber: number | null;
  public playerName: string;
  private websocketSub: Subscription;

  constructor(private _websocketService: WebsocketService,
    private _router: Router) { }

  ngOnDestroy(): void {
    this.websocketSub?.unsubscribe();
  }

  joinRoom() {
    this._websocketService.connectToRoom(this.roomNumber as number);
    this.websocketSub = this._websocketService.subscribeToTopic("player_number").subscribe(a => {

      this._websocketService.sendMessage("setPlayer", { id: (a as any)['playerId'], name: this.playerName })
      this._router.navigate(['game']);

    })
  }
}
