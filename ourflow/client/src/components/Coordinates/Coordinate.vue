<template>
  <div class="container-coordinates">
    <div
      class="columns is-multiline is-8"
      v-for="( itemCoo,index) in $store.getters.getDataCoordinate.item"
      :key="index"
    >
      <div class="column is-2">
        <div class="container-flex-center is-fullcentered">
          <figure class="image">
            <img :src="itemCoo.media_item" :alt="itemCoo.alt_item">
          </figure>
        </div>
      </div>
      <div class="column is-10">
        <div class="container-flex-center is-fullcentered">
          <div class="content full-width-content has-text-left has-text-centered-mobile">
            <a :href="itemCoo.link_item">{{itemCoo.descritpion_item}}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Coordinate"
};
</script>
