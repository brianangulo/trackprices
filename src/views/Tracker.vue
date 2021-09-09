<template>
  <div class="tracker">
    <h1>Track Your Shopping List</h1>
    <input id="add" ref="add" type="text">
    <button @click="addItem()">Add Item</button>
    <ul class="shop-list">
      <li v-for="item, index in list" :key="index" class="item"><input :id="item.id" type="checkbox" /> {{ item.name }} </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Tracker",
  data() {
    return {
      list: []
    }
  },
  methods: {
   async fetchShoppingList() {
      const response = await fetch("http://127.0.0.1:5000/hello");
      this.$data.list = JSON.parse((await response.text()));
    },
    saveShoppingItem: async (item) => {
      const response = await fetch("http://127.0.0.1:5000/hello", {
        method: "POST",
        body: JSON.stringify(item)
      });
      console.log(response);
    },
    addItem() {
      const inputEl = this.$refs.add;
      if (inputEl.value) {
        const tempList = [...this.$data.list];
        tempList.push({
          name: inputEl.value,
          id: Math.floor(Math.random() * 20)
        });
        this.$data.list = [...tempList];
        inputEl.value = "";
        this.saveShoppingItem()
      }
    }
  },
  mounted() {
    this.fetchShoppingList();
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
