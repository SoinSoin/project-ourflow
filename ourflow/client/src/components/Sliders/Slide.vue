<template>
  <div class="swiper-slide no-left">
    <slot></slot>
  </div>
</template>
<script>
export default {
  name: "Slide",
  props: {
    text: String
  }
};
</script>
<style>
.no-left{
  left:0 !important
}
</style>
