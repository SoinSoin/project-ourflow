<template>
  <nav class="hero is-warning nav-mobile">
    <div class="hero-body">
      <div class="container">
        <div
          class="menu-item-mobile has-text-white is-capitalized"
          v-for="(item, index) in itemsNav"
          :key="index"
          @click="passIndexNavToBody(index)"
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
  props: {
    itemsNav: Array
  },
  methods: {
    passIndexNavToBody(indexNavSlide) {
       this.$store.commit('updateIindexNavSlide', indexNavSlide)
    }
  }
};
</script>
<style lang="scss">
.nav-mobile {
  position: fixed;
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
