<template>
  <div id="main-prestation">
    <Section :hasColor="0" :title="$store.getters.getPage[$store.getters.getIndex] ">
      <article style="width:100%; height:20vh;" class="section has-background-warning"></article>
    </Section>
  </div>
</template>
<script>
import Section from "@/components/Sections/Section.vue";
export default {
  name: "Prestation",
  components: {
    Section
  }
};
</script>
<style lang="scss">
#main-prestation {
  section {
    padding-left: 0 !important;
    padding-right: 0 !important;
    .container {
      margin: 0 !important;
      width: 100%;
      max-width: 100%;
    }
    article {
      padding-top: 0 !important;
      padding-bottom: 0 !important;
    }
  }
}
</style>


