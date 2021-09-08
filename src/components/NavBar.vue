<template>
  <div class="navbar">
    <ul class="nav-ul">
      <li class="nav-li">
        <a href="">Tracker</a>
      </li>
      <li class="nav-li">
        <a href="">Login</a>
      </li>
      <li class="nav-li">
        <a href="">Logout</a>
      </li>
      <li class="nav-li">
        <a href="">Sign Up</a>
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
    margin: 0%;
  .nav-ul {
    top: 0; 
    display: flex;
    justify-content: space-evenly;
    .nav-li {
      list-style: none;
      a {
        color: black;
        text-decoration: none;
      }
    }
  }
}
</style>
