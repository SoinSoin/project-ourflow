<template>
  <!-- desktop List -->
  <article
    :class="{'hero':true,'is-medium':true, 'has-background-warning':isToRight%2,'has-background-white':!(isToRight%2), 'contain-section':true, 'container-list':true}"
  >
    <div class="hero-body hero-list">
      <div class="container" v-if="$store.getters.getSize >767">
        <div class="columns is-8" v-if="isToRight%2">
          <div class="column is-3 is-fullcentered">
            <ImageList :fetchData="fetchData.item[0]"/>
          </div>
          <div class="column is-9 is-fullcentered">
            <TextList :fetchData="fetchData" :isArrowWhite="isToRight%2"/>
          </div>
        </div>
        <div class="columns is-8" v-else>
          <div class="column is-9 is-fullcentered">
            <TextList :fetchData="fetchData" :isArrowWhite="isToRight%2"/>
          </div>
          <div class="column is-3 is-fullcentered">
            <ImageList :fetchData="fetchData.item[0]"/>
          </div>
        </div>
      </div>
      <!-- responsive List -->
      <div class="container" v-else>
        <div class="columns is-8">
          <div class="column is-3 is-fullcentered">
            <ImageList :fetchData="fetchData.item[0]"/>
          </div>
          <div class="column is-9 is-fullcentered">
            <TextList :fetchData="fetchData" :isArrowWhite="isToRight%2"/>
          </div>
        </div>
      </div>
    </div>
    <div class="container-stencil-section">
      <AfterSection
        :class="{'stencil-section':true, 'stencil-background-yellow':!(isToRight%2)&&!isGrey, 'stencil-background-white':isToRight%2&&!isGrey}"
      />
    </div>
  </article>
</template>
<script>
import AfterSection from "@/components/Sections/AfterSection.vue";
import TextList from "./ContentLists/TextList.vue";
import ImageList from "./ContentLists/ImageList.vue";
export default {
  name: "List",
  components: {
    ImageList,
    AfterSection,
    TextList
  },
  props: {
    isToRight: Number,
    isStencilGrey: Number,
    fetchData: Object
  },
  data() {
    return {
      isGrey: Boolean
    };
  },
  created() {
    this.isGrey = this.isToRight + 1 === this.isStencilGrey ? true : false;
  }
};
</script>
<style lang="scss">
.space-li {
  padding: 0.5em 0;
}
</style>

