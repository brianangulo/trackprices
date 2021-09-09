<template>
  <div class="navbar">
    <ul class="nav-ul">
      <li class="nav-li">
        Tracker
      </li>
      <li class="nav-li">
        Login
      </li>
      <li class="nav-li">
        Logout
      </li>
      <li class="nav-li">
        Sign Up
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "NavBar",
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
    .nav-li {
      list-style: none;
    }
  }
}
</style>
