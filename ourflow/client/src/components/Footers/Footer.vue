<template>
  <footer class="footer has-background-grey-dark">
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-3">
          <Coordinate/>
        </div>
        <div class="column is-6 is-fullcentered">
          <div class="columns is-multiline">
            <div class="column is-12">
              <div class="breadcrumb is-centered has-color-white">
                <ul class="has-text-white">
                  <li
                    class="has-text-white"
                    v-for="(item, index) in $store.getters.getUrl"
                    :key="index"
                  >
                    <router-link class="is-capitalized" :to="item.url">{{item.page}}</router-link>
                  </li>
                </ul>
              </div>
            </div>
            <div class="column is-12">
              <div class="content">
                <p
                  class="has-text-white"
                >2019 - Site Designé par Jules Yebdri et développé par OurFlow®.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-3 is-fullcentered">
          <Rsociaux class="footer-rsociaux"/>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
import Rsociaux from "@/components/RSociaux/Rsociaux.vue";
import Coordinate from "@/components/Coordinates/Coordinate";
export default {
  name: "Footer",
  components: {
    Rsociaux,
    Coordinate
  },
  methods: {
    passIndex(index) {
      this.$store.commit("setIndex", index);
    }
  }
};
</script>
<style lang="scss">
.footer {
  position: relative;
  top: calc(100vh - 3px);
  a {
    color: #fff;
  }
  a:hover {
    color: rgba(255, 255, 255, 0.6);
  }
}
.footer-rsociaux {
  width: 100%;
  .rs {
    color: #fff;
    transition-duration: 0.3s;
  }
  .rs:hover {
    color: rgba(255, 255, 255, 0.6);
  }
  a {
    color: #fff;
  }
}
.breadcrumb {
  a {
    color: #fff !important;
  }
  a {
    &.router-link-exact-active {
      color: #e2d637 !important;
    }
  }
}
@media (max-width: 767px) {
  .breadcrumb {
    a {
      padding: 0 0.5em !important;
    }
  }
}
</style>
