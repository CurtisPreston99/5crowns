import { StringMap } from '@angular/compiler/src/compiler_facade_interface';
import { Injectable } from '@angular/core';
import { filter, map, Observable, Observer, Subject } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class WebsocketService {
    readonly url = "wss://crowns5.herokuapp.com/room/"
    private RawMessageSubject: Subject<string>;
    private socket: WebSocket;
    private MessageSubject: Subject<{ topic: string, arg: object }>;

    private state: Map<string, object> = new Map<string, object>()

    constructor() {
        this.RawMessageSubject = new Subject();
        this.MessageSubject = new Subject<{ topic: string, arg: object }>();
    }

    public connectToRoom(room: number) {
        this.socket = new WebSocket(this.url + room);

        // Listen for messages
        this.socket.addEventListener('message', (event) => {
            this.RawMessageSubject.next(event.data);
            this.parseWebSocketMessage(event.data);
        });
    }

    public sendMessage(topic: string, params: any) {
        let command = {"comandType":topic,"params":params}
        this.socket.send(JSON.stringify(command));
    }

    private parseWebSocketMessage(message: string) {
        let obj = JSON.parse(message)
        let event = obj['event'] as string;
        let payload = obj['payload']
        console.log(event, payload);
        this.state.set(event, payload)
        this.MessageSubject.next({ topic: event, arg: payload });
    }

    public subscribeToTopic(topic: string) {
        return this.MessageSubject.pipe(
            filter(a => a.topic == topic),
            map(a => a.arg)
        )
    }

    
    public subscribeToTopicTyped<T>(topic: string,type: { new(): T ;} ):Observable<T> {
        return this.MessageSubject.pipe(
            filter(a => a.topic == topic),
            map(a => a.arg),
            map(a => {
                let i = new type();
                Object.assign(i,a)
                return i;
            })
        )
    }
}



