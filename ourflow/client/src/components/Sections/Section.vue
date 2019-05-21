<template>
  <section
    :class="{'hero':true,'is-medium':true, 'has-background-warning':hasColor%2, 'contain-section':true}"
  >
    <div class="hero-body section-hero">
      <div class="container section-container">
        <div class="content">
          <h1
            :class="{'subtitle':true, 'is-1':true, 'is-size-2-mobile':true, 'is-capitalized':true, 'has-text-weight-light':true,'has-text-warning':!(hasColor%2),'has-text-white':hasColor%2}"
          >
            {{titleSec}}
            <span class="higlight-title"></span>
          </h1>
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
import AfterSection from "@/components/Stencils/AfterSection.vue";
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
    this.displayStencil = this.hasStencil === false ? false : true;
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
.higlight-title:after {
  content: "";
  display: block;
  width: 100%;
  height: 7rem;
  background-image: url("/img/stencil/sc_highlight_wave.svg");
  background-repeat: no-repeat;
  background-size: 6rem;
  background-position: center;
}

@media screen and (max-width: 767px) {
  .higlight-title:after {
    height: 6rem;
    background-size: 5rem;
  }
}
</style>