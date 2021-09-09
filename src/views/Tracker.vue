<template>
  <div class="tracker">
    <h1>Track Your Shopping List</h1>
    <ul class="shop-list">
      <li v-for="item, index in list" :key="index" class="item"><input :id="index" type="checkbox" /> {{ item }} </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Tracker",
  data() {
    return {
      list: ["bread", "milk", "water", "coffee"]
    }
  }
};
</script>

<style lang="scss">
.tracker {
  .shop-list {
    .item {
      list-style: none;
    }
  }
}
</style>
