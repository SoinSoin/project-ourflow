<template>
  <!-- desktop List -->
  <article
    :class="{'section':true, 'has-background-warning':isToRight%2,'has-background-white':!isToRight%2 }"
  >
    <div class="container" v-if="$store.getters.getSize >767">
      <div class="columns" v-if="isToRight%2">
        <div class="column is-4"></div>
        <div class="column is-8">
          <div class="content has-text-left">
            <ul>
              <li
                class="space-li"
                v-for="(valItem, index) in fetchData.item"
                :key="index"
              >{{valItem.descritpion_item}}</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="columns" v-else>
        <div class="column is-8">
          <div class="content has-text-left">
            <ul>
              <li
                class="space-li"
                v-for="(valItem, index) in fetchData.item"
                :key="index"
              >{{valItem.descritpion_item}}</li>
            </ul>
          </div>
        </div>
        <div class="column is-4"></div>
      </div>
    </div>
    <!-- responsive List -->
    <div class="container" v-else>
      <div class="columns">
        <div class="column is-4"></div>
        <div class="column is-8"></div>
      </div>
    </div>
  </article>
</template>
<script>
export default {
  name: "List",
  props: {
    isToRight: Number,
    fetchData: Object
  }
};
</script>
<style lang="scss">
.space-li {
  padding: 0.5em 0;
}
</style>

