<template>
  <nav class="hero is-warning nav-mobile">
    <div class="hero-body">
      <div class="container">
        <div
          class="menu-item-mobile has-text-white is-capitalized"
          v-for="(item, index) in $store.getters.getData"
          :key="index"
          @click="passIndex(index)"
        >
          <router-link
            class="title"
            v-if="item.order_page===1"
            :to="{name:'home'}"
          >{{item.title_page}}</router-link>
          <router-link
            class="title"
            v-else
            :to="{name:'contents',params:{page:item.title_page}}"
          >{{item.title_page}}</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  name: "ContainerNav",
  methods: {
    passIndex(indexNavSlide) {
      this.$store.commit("setIndex", indexNavSlide);
    }
  }
};
</script>
<style lang="scss">
.nav-mobile {
  position: fixed;
  overflow: auto;
  z-index: 20;
  width: 100vw;
  height: 100vh;
  top: 0;
}
.menu-item-mobile {
  margin: 50px 0;
  .router-link-exact-active {
    color: #21201f !important;
  }
}
</style>
