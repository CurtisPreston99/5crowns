import { Injectable } from '@angular/core';
import { Board } from './common/entities/board-state';
import { Player } from './entities/player';
import { WebsocketService } from './services/websocket.service';

@Injectable({
    providedIn: 'root'
})
export class GameStateManagementService {

    public Players: Player[] = [];

    public Board: Board;

    public PlayerInfo: Player;
    public PlayerNumber: number;

    public websocketSub: any;


    constructor(private _websocketService: WebsocketService) {

        this._websocketService.subscribeToTopic("state").subscribe(a => {
            let playerStatesJson: any[] = (a as any)["playerState"]
            let playerStates: Player[] = []
            playerStatesJson.forEach(player => {
                let p = new Player();
                Object.assign(p, player);
                if (p.id == this.PlayerInfo.id) {
                    this.PlayerInfo = p;
                }
                playerStates.push(p)
            });
            this.Players = playerStates;

            let b = new Board();
            Object.assign(b, (a as any)["boardState"]);
            this.Board = b;
        });
    }

    public joinRoom(roomId: number) {
        this._websocketService.connectToRoom(roomId);
        this.websocketSub = this._websocketService.subscribeToTopic("player_number").subscribe(a => {
            console.table(this.PlayerInfo)
            this.PlayerInfo.id = (a as any)['playerId']
            this.PlayerNumber = (a as any)['playerNum']
            this._websocketService.sendMessage("setPlayer", { id: (a as any)['playerId'], name: this.PlayerInfo.name })
        })
    }

    public startGame() {
        this._websocketService.sendMessage("startGame", {});
    }

    public takeFromDiscard() {
        this._websocketService.sendMessage("takeFromDiscard", {});
    }

    public takeFromDeck() {
        this._websocketService.sendMessage("takeFromDeck", {});
    }
}
