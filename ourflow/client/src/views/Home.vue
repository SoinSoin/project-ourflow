<template>
  <div class="home">
    <Button :msg="'ceci est un composant boutton'"/>
    <h1>ceci est un composant de type views c'est comme une page</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import Button from '@/components/Button/Index.vue'

export default {
  name: 'home',
  components: {
    Button
  }
}
</script>
