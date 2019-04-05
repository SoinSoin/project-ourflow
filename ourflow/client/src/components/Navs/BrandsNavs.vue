<template>
  <div id="nav-brand">
    <router-link :to="{name:'home'}">
      <figure
        v-for="(data, index) in fetchData"
        :key="index"
        @click="passIndex(0)"
        class="image is-48x96"
      >
        <img :src="data.media_item" :alt="data.alt_item">
      </figure>
    </router-link>
  </div>
</template>
<script>
import getApi from "@/services/api.js";
export default {
  name: "BrandNav",
  data() {
    return {
      fetchData: []
    };
  },
  beforeMount() {
    this.fetchingData();
  },
  methods: {
    fetchingData() {
      getApi.getNav().then(res => {
        res.data.map(val => {
          this.fetchData = val.item;
        });
      });
    },
    passIndex(index) {
      this.$store.commit("updateIindexNavSlide", index);
    }
  }
};
</script>
<style lang="scss">
#nav-brand {
  position: absolute;
  top: 0;
  margin: 1vh;
}
.is-48x96 {
  height: 48px;
  width: 96px;
}
</style>
