<template>
  <a
    v-if="hasType='slide'"
    @click="smoothDown()"
    class="button modify-button is-danger is-outlined is-rounded"
  >
    <span class="has-text-weight-semibold">{{valueBtn}}</span>
    <span class="icon is-small">
      <fa-icon :icon="{prefix: 'fas', iconName:'long-arrow-alt-down'}"/>
    </span>
  </a>
  <a v-else class="button modify-button is-danger is-outlined is-rounded">
    <span class="has-text-weight-semibold">{{valueBtn}}</span>
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
    smoothDown() {}
  }
};
</script>

<style lang="scss">
.modify-button {
  font-family: "Montserrat", sans-serif;
  padding: 0.4em 1.6em !important;
  height: 1.2em !important;
  transition-duration: 0.3s;
}

.button:hover {
  background-color: red;
  color: white;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
}
//ne fonctionne pas 
// @media screen and (max-width: 767px) {
//   .modify-button {
//     padding: 0.2 0.8em !important;
//   }
// }
</style>