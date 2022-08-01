import { Injectable } from '@angular/core';
import { Observable, Observer, Subject } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class WebsocketService {
    readonly url = "wss://crowns5.herokuapp.com/room/"
    private RawMessageSubject: Subject<string>;
    private socket: WebSocket;

    constructor() {
        this.RawMessageSubject = new Subject();
    }

    public connectToRoom(room: number) {
        this.socket = new WebSocket(this.url + room);

        // Listen for messages
        this.socket.addEventListener('message', (event) => {
            this.RawMessageSubject.next(event.data);
        });
    }

    private parseWebSocketMessage(message: string) {
        
    }

    public subscribeToTopic(topic: string) {

    }
}



