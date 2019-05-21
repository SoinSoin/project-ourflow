<template>
  <nav class="navbar nav-navbar bg-nav">
    <div class="navbar-brand size-nav">
      <div
        class="navbar-item menu-item is-capitalized"
        v-for="(item, index) in $store.getters.getUrl"
        :key="index"
      >
        <router-link :to="item.url">{{item.page}}</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  data() {
    return {
      index: Number
    };
  }
};
</script>

<style lang="scss">
nav {
  &.navbar {
    z-index: 0;
  }
}
.nav-navbar {
  position: fixed !important;
  right: -1px;
  top: 0;
}

.bg-nav {
  position: fixed !important;
  right: -1px;
  top: 0;
}
.bg-nav::before {
  content: "";
  position: absolute;
  background-image: url("/img/background/bg_menu.svg");
  filter: drop-shadow(0 0 10px rgba(0, 0, 0, 0.3));
  background-repeat: no-repeat;
  background-size: cover;
  width: 125%;
  height: 175%;
  right: 0;
}
.menu-item a {
  color: #000;
  margin: 0 5px 0 5px;
}
.router-link-exact-active {
  color: #e2d637 !important;
}

.menu-item a::before {
  content: "";
  position: absolute;
  width: 0;
  height: 3px;
  right: -4px;
  left: auto;
  bottom: 10px;
  background-color: #e2d637;
  border-radius: 2px;
}

.menu-item a:hover::before {
  width: calc(100% - 0.75rem);
  left: 0.375em;
  right: auto;
}

.menu-item a::before {
  transition-duration: 0.4s;
  transition-timing-function: cubic-bezier(0.34, 0.68, 0.2, 0.97);
}
</style>
