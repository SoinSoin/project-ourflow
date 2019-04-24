<template>
  <!-- desktop List -->
  <article
    :class="{'hero':true,'is-medium':true, 'has-background-warning':isToRight%2,'has-background-white':!(isToRight%2), 'contain-section':true, 'container-list':true}"
  >
    <div class="hero-body hero-list">
      <div class="container">
        <div :class="{'columns':true,  'is-8':true, 'is-direction-column':true}" v-if="isToRight%2">
          <div class="column is-3 is-fullcentered">
            <ImageList :fetchData="fetchData.item[0]"/>
          </div>
          <div class="column is-9 is-fullcentered">
            <TextList :fetchData="fetchData" :isArrowWhite="isToRight%2"/>
          </div>
        </div>

        <div
          :class="{'columns':true,  'is-8':true, 'is-direction-column':true,'is-direction-column-resp':!(isToRight%2)}"
          v-else
        >
          <div class="column is-9 is-fullcentered">
            <TextList :fetchData="fetchData" :isArrowWhite="isToRight%2"/>
          </div>
          <div class="column is-3 is-fullcentered">
            <ImageList :fetchData="fetchData.item[0]"/>
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
import AfterSection from "@/components/Stencils/AfterSection.vue";
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
.is-direction-column {
  position: relative;
  display: flex;
  flex-direction: row;
}
@media screen and (max-width: 767px) {
  .is-direction-column {
    flex-direction: column;
  }
  .is-direction-column-resp {
    flex-direction: column-reverse !important;
  }
}
</style>

