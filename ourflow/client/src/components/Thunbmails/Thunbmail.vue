<template>
  <div class="item-thunbmail columns is-multiline">
    <div class="column is-12 is-fullcentered">
      <figure class="image is-128x128">
        <img class="is-rounded" :src="dataFetch.media_item" :alt="dataFetch.alt_item">
      </figure>
    </div>
    <div class="column is-12 is-fullcentered">
      <div class="content content has-text-centered has-text-grey-dark">
        <h3 class="title is-4 is-size-5-mobile">
          <span class="highlight-title-is-3 highlight-title-is-3-white">{{dataFetch.title_item}}</span>
        </h3>
        <h4 class="subtitle is-5 is-size-6-mobile has-text-white">{{dataFetch.descritpion_item}}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Thunbmail",
  props: {
    dataFetch: Object
  }
};
</script>
<style lang="scss">
.item-thunbmail {
  .image {
    img {
      height: 100%;
      box-shadow: 0px 0px #fff, 0px 0px #fff, 1px 1px #fff, 4px 4px #fff,
        2px 2px #fff, 3px 3px #fff, 4px 4px #fff, 5px 5px #fff;
    }
  }
}
</style>

