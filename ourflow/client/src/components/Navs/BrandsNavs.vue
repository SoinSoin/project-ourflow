<template>
  <router-link id="nav-brand" :to="$store.getters.getUrl[0].url">
    <figure class="image is-48x96">
      <img src="/img/logo_ourflow.svg" alt="logo OurFlow">
    </figure>
  </router-link>
</template>
<script>
export default {
  name: "BrandNav"
};
</script>
<style lang="scss">
#nav-brand {
  position: absolute;
  margin: 10px;
}
@media screen and (max-width: 1024px) {
  #nav-brand {
    top: 0;
  }
}
.is-48x96 {
  height: 48px;
  width: 96px;
}
</style>
