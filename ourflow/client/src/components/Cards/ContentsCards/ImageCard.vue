<template>
  <figure
    class="bg-half-card"
    :style="{'background-image':`url(${dataCard.item[0].media_item})`}"
    :alt="dataCard.item[0].alt_item"
  >
    <slot/>
  </figure>
</template>
<script>
export default {
  name: "ImageCard",
  props: { dataCard: Object }
};
</script>
<style lang="scss">
.bg-half-card {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 40% !important;
}
</style>
