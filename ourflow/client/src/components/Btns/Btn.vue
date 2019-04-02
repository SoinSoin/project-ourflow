<template>
  <a
    v-if="hasType='slide'"
    @click="smoothDown()"
    class="button modify-button is-danger is-outlined is-rounded"
  >
    <span class="has-text-weight-semibold is-size-6-mobile">{{valueBtn}}</span>
    <span class="icon is-small">
      <fa-icon :icon="{prefix: 'fas', iconName:'long-arrow-alt-down'}"/>
    </span>
  </a>
  <a v-else class="button modify-button is-danger is-outlined is-rounded">
    <span class="has-text-weight-semibold is-size-6-mobile">{{valueBtn}}</span>
  </a>
</template>
​
<script>
export default {
  props: {
    valueBtn: String,
    hasType: String
  },
  methods: {
    smoothDown() {
      window.scroll({
        top: document.getElementById("main-pages").offsetTop,
        left: 0,
        behavior: "smooth"
      });
      // id="main-pages"
    }
  }
};
</script>

<style lang="scss">
a {
  &.button {
    &.is-rounded {
      &.modify-button {
        font-family: "Montserrat", sans-serif;
        transition-duration: 0.3s;
        padding: 0.4em 1.6em;
        height: 1.2em;
      }
    }
  }
}
.modify-button:hover {
  background-color: red;
  color: white;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
}
//ne fonctionne pas
@media screen and (max-width: 767px) {
a {
  &.button {
    &.is-rounded {
      &.modify-button {
        padding: 0.2em 0.8em;
        height: 1em;
      }
    }
  }
}
}
</style>