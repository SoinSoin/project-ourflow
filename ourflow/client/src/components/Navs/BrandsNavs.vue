<template>
  <div id="nav-brand">
    <router-link :to="{name:'home'}">
      <figure @click="passIndex(0)" class="image is-48x96">
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
  },
  methods: {
    passIndex(index) {
      this.$store.commit("setIndex", index);
    }
  }
};
</script>
<style lang="scss">
#nav-brand {
  position: absolute;
  top: -10px;
  margin: 0 0.5em;
}
.is-48x96 {
  height: 48px;
  width: 96px;
}
</style>
