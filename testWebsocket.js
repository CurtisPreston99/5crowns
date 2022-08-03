// Create WebSocket connection.
const socket = new WebSocket('wss://crowns5.herokuapp.com/room/22');

// Connection opened
socket.addEventListener('open', function (event) {
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
});

socket.send('{"comandType":"startGame","params":{}}')
socket.send('{"comandType":"takeFromDeck","params":{}}')
