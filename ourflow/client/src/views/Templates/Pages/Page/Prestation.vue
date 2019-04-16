<template>
  <div id="main-prestation">
    <Section
      :hasColor="0"
      :titleSec="$store.getters.getPage[$store.getters.getIndex]"
      :hasStencil="false"
    >
      <List
        v-for="(valPara, index) in fetchData.paragraph"
        :key="index"
        :isToRight="index"
        :fetchData="valPara"
      />
    </Section>
  </div>
</template>
<script>
import Section from "@/components/Sections/Section.vue";
import List from "@/components/Lists/List.vue";
export default {
  name: "Prestation",
  components: {
    List,
    Section
  },
  props: {
    fetchData: Object
  },
  beforeMount() {
    console.log(this.fetchData);
  }
};
</script>
<style lang="scss">
#main-prestation {
  section {
    padding-left: 0 !important;
    padding-right: 0 !important;
    padding-bottom: 0 !important;
    .section-container {
      margin: 0;
      width: 100%;
      max-width: 100%;
    }
  }
}
</style>


