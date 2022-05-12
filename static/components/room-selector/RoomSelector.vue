<script>
import myInstance from "../../services/my-singleton.mjs";

export default {
  data() {
    return {
      msg: "world!",
      color: "blue",
      room: 0,
      socket: new myInstance(),
    };
  },
  methods: {
    logRoom() {
      console.log(this.socket.name);
      console.log(this.socket.data());
    },
  },
};
</script>

<style scoped>
.example {
  color: v-bind("color");
}
</style>
<template>
  <h2>enter a room number</h2>
  <input type="number" v-model="room" min="0" max="9999" />
  <button @click="logRoom">join</button>
</template>
