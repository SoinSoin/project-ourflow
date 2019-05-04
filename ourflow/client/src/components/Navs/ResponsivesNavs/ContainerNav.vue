<template>
  <nav class="hero is-warning nav-mobile">
    <div class="hero-body">
      <div class="container">
        <div
          class="menu-item-mobile has-text-white is-capitalized"
          v-for="(item, index) in $store.getters.getUrl"
          :key="index"
        >
          <router-link class="title" :to="item.url">{{item.page}}</router-link>
        </div>
        <div class="menu-item-mobile">
          <Rsociaux/>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import Rsociaux from "@/components/RSociaux/Rsociaux.vue";
export default {
  name: "ContainerNav",
  components: {
    Rsociaux
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
