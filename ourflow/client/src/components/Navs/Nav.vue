<template>
  <nav class="navbar nav-navbar">
    <div class="navbar-brand size-nav">
      <div
        class="navbar-item menu-item is-capitalized"
        v-for="(item, index) in $store.getters.getUrl"
        :key="index"
      >
        <router-link :to="item.url">{{item.page}}</router-link>
      </div>
    </div>
    <span class="bg-nav" :style="{'background-image':`url(${publicPath}background/bg_menu.svg )`}"></span>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  data() {
    return {
      publicPath: process.env.VUE_APP_BASE_IMG,
      index: Number
    };
  },
  beforeMount() {
    console.log(this.$store.getters.getUrl);
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
  position: absolute;
  filter: drop-shadow(0 0 10px rgba(0, 0, 0, 0.3));
  background-repeat: no-repeat;
  background-size: cover;
  width: 125%;
  height: 175%;
  right: 0;
  top: 0;
  z-index: -1;
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
