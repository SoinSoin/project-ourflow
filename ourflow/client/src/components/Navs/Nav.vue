<template>
  <nav class="navbar bg-nav">
    <div class="navbar-brand size-nav">
      <div
        class="navbar-item menu-item is-capitalized"
        v-for="(item, index) in itemsNav"
        :key="index"
        @click="passIndexNavToBody(index)"
      >
        <router-link v-if="item.order_page===1" :to="{name:'home'}">{{item.title_page}}</router-link>
        <router-link
          v-else
          :to="{name:'contents',params:{page:item.title_page}}"
        >{{item.title_page}}</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  props: {
    itemsNav: Array
  },
  methods: {
    passIndexNavToBody(indexNavSlide, event) {
      this.$emit("returnNavToBody", indexNavSlide);
    }
  }
};
</script>

<style lang="scss">
.bg-nav {
  position: fixed !important;
  z-index: 30 !important;
  right: -1px;
  top: 0;
}

.bg-nav::before {
  content: "";
  position: absolute;
  background-image: url("/img/background_menu.svg");
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
  width: calc(100% + 8px);
  left: -4px;
  right: auto;
}

.menu-item a::before {
  transition-duration: 0.4s;
  transition-timing-function: cubic-bezier(0.34, 0.68, 0.2, 0.97);
}
</style>
