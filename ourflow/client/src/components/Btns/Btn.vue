<template>
  <a v-if="hasType==='slide'" class="button modify-button is-danger is-outlined is-rounded is-uppercase">
    <span class="has-text-weight-semibold is-size-6-mobile">{{valueBtn}}</span>
    <span class="icon is-small">
      <fa-icon :icon="{prefix: 'fas', iconName:'long-arrow-alt-down'}"/>
    </span>
  </a>
  <a
    v-else-if="hasType==='modal' && $store.getters.getSize<768"
    class="button is-medium close-modal modify-button is-danger is-outlined is-paddingless is-marginless is-fullcentered"
  >
    <span class="icon">
      <fa-icon :icon="{prefix: 'fas', iconName:'times'}"/>
    </span>
  </a>
  <a v-else class="button modify-button is-danger is-outlined is-rounded is-uppercase is-fullcentered">
    <span class="has-text-weight-semibold is-size-6-mobile">{{valueBtn}}</span>
  </a>
</template>
​
<script>
export default {
  props: {
    valueBtn: String,
    hasType: String
  }
};
</script>

<style lang="scss">
a {
  &.button {
    &.close-modal {
      border-radius: 50%;
      width: 40px;
      height: 40px;
    }
    &.is-rounded {
      &.modify-button {
        font-family: "Montserrat", sans-serif;
        transition-duration: 0.3s;
        padding: 0 1.6em;
        height: 1.8em;
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
          padding: 0 0.8em;
          height: 1.4em;
        }
      }
    }
  }
}
</style>