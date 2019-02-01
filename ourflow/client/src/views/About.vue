<template>
  <div class="about">
    <fa-icon fas icon="user" size="3x"/>
      <h1>ceci est un composant de type views c'est comme une page</h1>
    <Section/>
  </div>
</template>

<script>
import Section from '@/components/Section/Index.vue'
export default {
  name: 'about',
  components: {
    Section
  }
}
</script>
