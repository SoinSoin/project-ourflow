<template>
  <article class="card">
    <div class="columns is-gapless">
      <div v-if="$store.getters.getSize >769" class="column is-6">
        <ImageCard v-if="isToRight % 2" :dataCard="fetchDataCard" class="to-right"/>
        <TextCard v-else :dataCard="fetchDataCard"/>
      </div>
      <div v-else class="column is-6">
        <ImageCard :dataCard="fetchDataCard" class="to-right"/>
      </div>
      <div v-if="$store.getters.getSize>769" class="column is-6">
        <TextCard v-if="isToRight % 2" :dataCard="fetchDataCard"/>
        <ImageCard v-else :dataCard="fetchDataCard" class="to-left"/>
      </div>
      <div v-else class="column is-6">
        <TextCard :dataCard="fetchDataCard"/>
      </div>
    </div>
  </article>
</template>
​
<script>
import ImageCard from "./ContentsCards/ImageCard.vue";
import TextCard from "./ContentsCards/TextCard.vue";
export default {
  props: {
    fetchDataCard: Object,
    isToRight: Number
  },
  components: {
    ImageCard,
    TextCard
  }
};
</script>

<style lang="scss">
article {
  &.card {
    overflow: hidden;
    margin: 0 auto 20% auto;
    border-radius: 10px;
    max-width: 80%;
    box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
  }
}
.to-right:before {
  content: "";
  background-image: url("/img/vague_carte_portfolio.svg");
  background-size: contain;
  background-repeat: no-repeat;
  position: absolute;
  height: 102%;
  width: 50%;
  top: -1%;
  right: 45%;
  transform: rotate(180deg);
}

.to-left:before {
  content: "";
  background-image: url("/img/vague_carte_portfolio.svg");
  background-size: contain;
  background-repeat: no-repeat;
  position: absolute;
  height: 102%;
  width: 50%;
  top: -1%;
  left: 45%;
}

@media screen and (max-width: 769px) {
  .to-right:before {
    height: 65%;
    width: 100%;
    top: -5%;
    right: 0;
    transform: rotate(270deg);
  }
}
</style>