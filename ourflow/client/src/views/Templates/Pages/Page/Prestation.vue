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
        :isStencilGrey="fetchData.paragraph.length"
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
  .hero {
    .section-hero {
      padding-left: 0;
      padding-right: 0;
      padding-bottom: 0;
      .section-container {
        margin: 0;
        width: 100%;
        max-width: 100%;
      }
    }
  }
}

#main-prestation {
  .hero:first-child {
    .section-hero:first-child {
      padding-left: 0;
      padding-right: 0;
      padding-bottom: 0;
      .section-container:first-child {
        margin: 0;
        width: 100%;
        max-width: 100%;
        .container-list:nth-child(2) {
          .hero-list {
            padding-top: 0;
          }
        }
      }
    }
  }
}

// #main-prestation
//   section:first-child
//   .hero-body:first-child
//   .container:first-child
//   article:first-child
//   .hero-body:first-child {
//   padding-top: 0;
// }
</style>


