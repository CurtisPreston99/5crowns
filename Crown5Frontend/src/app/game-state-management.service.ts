import { Injectable } from '@angular/core';
import { Player } from './entities/player';
import { WebsocketService } from './services/websocket.service';

@Injectable({
    providedIn: 'root'
})
export class GameStateManagementService {

    public Players: Player[] = [];
    public : Player[] = [];

    constructor(private _websocketService: WebsocketService) {

        this._websocketService.subscribeToTopic("state").subscribe(a => {
            let playerStatesJson: any[] = (a as any)["playerState"]
            let playerStates: Player[] = []
            playerStatesJson.forEach(player => {
                let p = new Player();
                Object.assign(p, player);
                playerStates.push(p)
            });
            this.Players = playerStates;

            let boardState = a as any["boardState"]
        });
    }

    public startGame(){
        this._websocketService.sendMessage("startGame",{});
    }
}
