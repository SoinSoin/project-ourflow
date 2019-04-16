<template>
  <div :id="`main-${$store.getters.getPage[$store.getters.getIndex]}`">
    <Section
      v-for="(para,index) in fetchData.paragraph"
      :hasStencil="true"
      :key="index"
      :hasColor="index"
      :titleSec="para.title_para"
    >
      <article :id="`main-${para.title_para}`" v-if="index == 0">
        <div class="columns" v-for="(item, indexItem) in para.item" :key="indexItem">
          <div class="column is-4">
            <figure class="image">
              <img :src="item.media_item" :alt="item.alt_item">
            </figure>
          </div>
          <div class="column is-8 is-fullcentered">
            <div
              class="content full-width-content has-text-left has-text-centered-mobile has-text-grey-dark"
            >
              <p>{{item.descritpion_item}}</p>
            </div>
          </div>
        </div>
      </article>
      <article :id="`main-${para.title_para}`" v-if="index == 1">
        <div class="columns is-multiline">
          <div
            class="column is-3 is-fullcentered"
            v-for="(item, indexItem) in para.item"
            :key="indexItem"
          >
            <Thunbmail :dataFetch="item"/>
          </div>
        </div>
      </article>
      <article id="main-technologies" v-if="index == 2">
        <div class="columns is-multiline is-fullcentered">
          <div
            class="column is-2 is-fullcentered"
            v-for="(item, indexItem) in para.item"
            :key="indexItem"
          >
            <figure class="image" :title="item.title_item">
              <img :src="item.media_item" :alt="item.alt_item">
            </figure>
          </div>
        </div>
      </article>
    </Section>
  </div>
</template>
<script>
import Thunbmail from "@/components/Thunbmails/Thunbmail.vue";
import Section from "@/components/Sections/Section.vue";
export default {
  name: "Home",
  components: {
    Section,
    Thunbmail
  },
  props: {
    fetchData: Object
  },
  beforeMount() {
    console.log(this.fetchData)
  },
};
</script>
<style lang="scss">
@media (max-width: 767px) {
  #main-technologies {
    .is-fullcentered {
      flex-direction: column;
    }
  }
}
</style>


