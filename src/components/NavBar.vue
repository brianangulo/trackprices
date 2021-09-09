<template>
  <div class="navbar">
    <ul class="nav-ul">
      <li class="nav-li">
       <button @click="goTo('/hello')">Tracker</button>
      </li>
      <li class="nav-li">
        <button @click="goTo('/hello')">Login</button> 
      </li>
      <li class="nav-li">
       <button @click="goTo('/hello')">Logout</button>
      </li>
      <li class="nav-li">
       <button @click="goTo('/hello')">Sign Up</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
   
  }
};
</script>

<style lang="scss">
.navbar {
  background-color: lightblue;
  .nav-ul {
    top: 0;
    display: flex;
    justify-content: space-evenly;
    margin: 0px;
    padding: 3%;
    .nav-li {
      list-style: none;
    }
  }
}
</style>
