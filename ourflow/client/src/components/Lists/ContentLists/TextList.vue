<template>
  <div class="content has-text-left full-width-content content-list-text">
    <h3 class="title is-3 is-size-4-mobile has-text-centered-mobile is-capitalized">
      <span
        :class="{'highlight-title-is-3':true, 'highlight-title-is-3-white':isArrowWhite,'highlight-title-is-3-yellow':!isArrowWhite}"
      >{{fetchData.title_para}}</span>
    </h3>
    <ul class="fa-ul">
      <li class="space-li" v-for="index in fetchData.item.length-1" :key="index">
        <span class="fa-li">
          <fa-icon
            :class="{'has-text-white':isArrowWhite, 'has-text-warning': !isArrowWhite, 'size-style-list':true}"
            :icon="{ prefix: 'fas', iconName: 'long-arrow-alt-right' }"
          />
        </span>
        {{fetchData.item[index].descritpion_item}}
      </li>
    </ul>
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