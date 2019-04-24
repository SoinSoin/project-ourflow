<template>
  <!--desktop Card-->
  <article class="card contain-section">
    <div
      :class="{'columns':true,  'is-gapless':true, 'is-direction-column':true, 'is-direction-column-resp':!(isToRight%2)}"
    >
      <div class="column is-6">
        <ImageCard v-if="isToRight % 2" :dataCard="fetchDataCard" class="to-right">
          <StencilPortfolio class="stencil-background-white"/>
        </ImageCard>
        <TextCard v-else :dataCard="fetchDataCard">
          <slot/>
        </TextCard>
      </div>
      <div class="column is-6">
        <TextCard v-if="isToRight % 2" :dataCard="fetchDataCard">
          <slot/>
        </TextCard>
        <ImageCard v-else :dataCard="fetchDataCard" class="to-left">
          <StencilPortfolio class="stencil-background-white"/>
        </ImageCard>
      </div>
    </div>
  </article>
</template>
​
<script>
import StencilPortfolio from "@/components/Stencils/StencilPortfolio.vue";
import ImageCard from "./ContentsCards/ImageCard.vue";
import TextCard from "./ContentsCards/TextCard.vue";
export default {
  name: "Card",
  components: {
    ImageCard,
    StencilPortfolio,
    TextCard
  },
  props: {
    fetchDataCard: Object,
    isToRight: Number
  }
};
</script>

<style lang="scss">
article {
  &.card {
    overflow: hidden;
    margin: 0 auto 10vh auto;
    border-radius: 10px;
    max-width: 80%;
    box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
    .is-direction-column {
      position: relative;
      display: flex;
      flex-direction: row;
    }
  }
}
.to-right {
  position: relative;
  .main-stencil-portfolio {
    position: absolute;
    width: auto;
    height: 102%;
    top: -1%;
    left: 85%;
    transform: rotate(180deg);
  }
}
.to-left {
  position: relative;
  .main-stencil-portfolio {
    position: absolute;
    width: auto;
    height: 102%;
    top: -1%;
    left: -10%;
  }
}
@media screen and (max-width: 767px) {
  article {
    &.card {
      .is-direction-column {
        flex-direction: column;
      }
      .is-direction-column-resp {
        flex-direction: column-reverse !important;
      }
    }
  }
  .to-right {
    .main-stencil-portfolio {
      position: absolute;
      width: 102%;
      height: auto;
      top: 80%;
      left: -1%;
      transform: rotate(180deg);
    }
  }
  .to-left {
    .main-stencil-portfolio {
      position: absolute;
      width: 102%;
      height: auto;
      top: 80%;
      left: -1%;
      transform: rotate(180deg);
    }
  }
}
</style>