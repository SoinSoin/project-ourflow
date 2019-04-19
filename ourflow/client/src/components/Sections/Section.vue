<template>
  <section
    :class="{'hero':true,'is-medium':true, 'has-background-warning':hasColor%2, 'contain-section':true}"
  >
    <div class="hero-body section-hero">
      <div class="container section-container">
        <div class="content">
          <h1
            :class="{'higlight-title':true, 'subtitle':true, 'is-1':true, 'is-size-2-mobile':true, 'is-capitalized':true, 'has-text-weight-light':true,'has-text-warning':!(hasColor%2),'has-text-white':hasColor%2}"
          >{{titleSec}}</h1>
        </div>
        <slot/>
      </div>
    </div>
    <div class="container-stencil-section" v-if="displayStencil">
      <AfterSection
        :class="{'stencil-section':true, 'stencil-background-yellow':!(hasColor%2) &&!isGrey, 'stencil-background-white':hasColor%2&&!isGrey,}"
      />
    </div>
  </section>
</template>
<script>
import AfterSection from "./AfterSection.vue";
export default {
  name: "Section",
  components: {
    AfterSection
  },
  props: {
    hasStencil: true,
    hasColor: Number,
    lengthArr: Number,
    titleSec: String
  },
  data() {
    return {
      isGrey: false,
      displayStencil: Boolean
    };
  },

  beforeMount() {
    this.displayStencil = (this.hasStencil === false) ? false : true
    this.greying();
  },
  methods: {
    greying() {
      if (this.hasColor + 1 === this.lengthArr) this.isGrey = true;
    }
  }
};
</script>
<style lang="scss">

</style>