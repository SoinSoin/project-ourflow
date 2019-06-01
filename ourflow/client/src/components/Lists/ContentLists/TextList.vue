<template>
  <div class="content has-text-left full-width-content content-list-text">
    <h3 class="title is-3 is-size-4-mobile has-text-centered-mobile is-capitalized">
      <span
        :class="{'highlight-title-is-3':true, 'highlight-title-is-3-white':isArrowWhite,'highlight-title-is-3-yellow':!isArrowWhite}"
      >{{fetchData.title_para}}</span>
    </h3>
    <div class="columns is-multiline">
      <div class="column is-half" v-for="index in fetchData.item.length-1" :key="index">
        <div class="columns is-mobile">
          <div class="column is-2">
            <span class="container-flex-center is-fullcentered">
              <fa-icon
                :class="{'has-text-white':isArrowWhite, 'has-text-warning': !isArrowWhite, 'size-style-list':true}"
                :icon="{ prefix: 'fas', iconName: 'long-arrow-alt-right' }"
              />
            </span>
          </div>
          <div class="column is-10">
              <p class="has-text-weight-semibold">{{fetchData.item[index].descritpion_item}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "TextList",
  props: {
    fetchData: Object,
    isArrowWhite: Number
  }
};
</script>
<style lang="scss">
.content {
  .size-style-list {
    font-size: 1.5em;
  }
  li {
    list-style: none;
  }
}
</style>