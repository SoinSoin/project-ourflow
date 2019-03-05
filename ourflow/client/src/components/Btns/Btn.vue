<template>
  <a class="button is-danger is-outlined is-rounded">{{valueBtn}}</a>
</template>
​
<script>
export default {
  props: {
    valueBtn: String
  }
};
</script>

<style lang="scss">
.button {
  font-family: "Montserrat", sans-serif;
  padding-left: 40px !important;
  padding-right: 40px !important;
  transition-duration: 0.3s;
}

.button:hover {
  background-color: red;
  color: white;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
}
</style>