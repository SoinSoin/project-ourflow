<template>
<div :id="`main-${$store.getters.getPage[$store.getters.getIndex]}`">
    <Section :hasColor="0" :title="$store.getters.getPage[$store.getters.getIndex] "></Section>
</div>
</template>
<script>
import Section from "@/components/Sections/Section.vue";  
export default {
  name: "Prestation",
  components: {
    Section
  },
};
</script>

