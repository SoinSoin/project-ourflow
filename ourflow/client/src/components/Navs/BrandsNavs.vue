<template>
  <div id="nav-brand">
    <router-link :to="$store.getters.getUrl[0].url">
      <figure class="image is-48x96">
        <img :src="`${publicPath}logo_ourflow.svg`" alt="logo OurFlow">
      </figure>
    </router-link>
  </div>
</template>
<script>
export default {
  name: "BrandNav",
  data() {
    return {
      publicPath: process.env.VUE_APP_BASE_IMG
    };
  }
};
</script>
<style lang="scss">
#nav-brand {
  position: absolute;
  margin: 10px;

}
.is-48x96 {
  height: 48px;
  width: 96px;
}
</style>
