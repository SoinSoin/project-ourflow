<template>
  <nav class=navbar>
    <div class="navbar-brand">
      <div class="navbar-item" v-for="(item,  index) in itemsNav" :key="index" @click="getIndex(index)">
        <router-link v-if="item.linkto==='home'" class="item" :to="{name:'home'}">{{item.name}}</router-link>
        <router-link
          v-else
          class="navbar-item"
          :to="{name:'contents',params:{page:item.linkto}}"
        >{{item.name}}</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  props: {
    itemsNav: Array
  },
  // beforeCreate() {},
  methods: {
    getIndex(index, event) {
      this.$emit("clicked", index);
    }
  }
};
</script>

<style lang="scss">
nav {
  position: fixed;
  background: red;
  padding:1em;
  z-index: 30;
  a {
    font-weight: bold;
    color: #2c3e50;
  }
  .router-link-exact-active {
    color: #42b983;
  }
}
</style>
