<template>
  <div id="app">
    <Nav/>
    <router-view/>
  </div>
</template>

<script>
import Nav from '@/components/Nav/Index.vue'
// dans ce fichier on  va appeler seulement les elements qui sont su toute les pages exemples la barre de navigation et le footer
export default {
  components: {
    Nav
  }
}
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
