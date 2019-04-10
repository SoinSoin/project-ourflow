<template>
<div :id="`main-${$store.getters.getPage[$store.getters.getIndex]}`">
    <Section :hasColor="0"></Section>
</div>
</template>
<script>
import Section from "@/components/Sections/Section.vue";
export default {
  name: "Home",
  components: {
    Section
  },
};
</script>

