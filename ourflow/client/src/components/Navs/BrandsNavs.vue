<template>
  <div id="nav-brand">
    <router-link :to="{name:'home'}">
      <figure
        @click="passIndex(0)"
        class="image is-48x96"
      >
        <img src="/img/logo_ourflow.svg" alt="logo de OurFlow">
      </figure>
    </router-link>
  </div>
</template>
<script>
export default {
  name: "BrandNav",
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
  top: -5vh;
  margin: 1vh;
}
.is-48x96 {
  height: 48px;
  width: 96px;
}
</style>
