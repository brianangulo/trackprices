<template>
  <div class="tracker">
    <h1>Track Your Shopping List</h1>
    <input id="add" ref="add" type="text" />
    <button @click="addItem()">Add Item</button>
    <ul class="shop-list">
      <li v-for="(item, index) in list" :key="index" class="item">
        <input :id="index" type="checkbox" /> {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Tracker",
  data() {
    return {
      list: [],
    };
  },
  methods: {
    async fetchShoppingList() {
      const response = await fetch("http://127.0.0.1:5000/hello");
      this.$data.list = JSON.parse(await response.text());
    },
    async saveShoppingItem(item) {
      const response = await fetch("http://127.0.0.1:5000/hello", {
        method: "POST",
        body: JSON.stringify(item),
      });
      console.log(await response.text());
    },
    addItem() {
      const inputEl = this.$refs.add;
      if (inputEl.value) {
        const tempList = [...this.$data.list];
        const listItem = {
          name: inputEl.value,
        };
        tempList.push(listItem);
        this.$data.list = [...tempList];
        this.saveShoppingItem(listItem);
        inputEl.value = "";
      }
    },
  },
  mounted() {
    this.fetchShoppingList();
  },
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
