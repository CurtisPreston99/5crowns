<script>
import RoomSelector from "./room-selector/RoomSelector.vue";

export default {
  components: {
    RoomSelector,
  },
  data() {
    return {
      msg: "world!",
      color: "blue",
    };
  },
};
</script>

<style scoped>
.example {
  color: v-bind("color");
}
</style>

<template>
  <span class="example">{{ msg }}</span>
  <room-selector></room-selector>
</template>
