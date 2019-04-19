<template>
  <figure class="image">
    <img :src="fetchData.media_item" :alt="fetchData.alt_item">
  </figure>
</template>
<script>
export default {
  name: "ImageList",
  props: {
    fetchData: Object
  }
};
</script>
<style lang="scss">
</style>
