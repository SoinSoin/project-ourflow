<template>
  <footer class="footer has-background-grey-dark">
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-3">
          <div
            class="columns is-multiline"
            v-for="i in $store.getters.getData[3].paragraph[0].item.length-1"
            :key="i"
          >
            <div class="column is-2 is-fullcentered">
              <figure class="image">
                <img
                  :src="$store.getters.getData[3].paragraph[0].item[i].media_item"
                  :alt="$store.getters.getData[3].paragraph[0].item[i].alt_item"
                >
              </figure>
            </div>
            <div class="column is-10 is-fullcentered">
              <div
                class="content full-width-content has-text-left has-text-centered-mobile has-text-white"
              >
                <a
                  class="has-text-white"
                  :href="$store.getters.getData[3].paragraph[0].item[i].link_item"
                >{{$store.getters.getData[3].paragraph[0].item[i].descritpion_item}}</a>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-6 is-fullcentered">
          <div class="columns is-multiline">
            <div class="column is-12">
              <div class="breadcrumb is-centered has-color-white">
                <ul class="has-text-white">
                  <li
                    class="has-text-white"
                    v-for="(item, index) in $store.getters.getData"
                    :key="index"
                    @click="passIndex(index)"
                  >
                    <router-link v-if="item.order_page===1" :to="{name:'home'}">{{item.title_page}}</router-link>
                    <router-link
                      v-else
                      :to="{name:'contents',params:{page:item.title_page}}"
                    >{{item.title_page}}</router-link>
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

export default {
  name: "Footer",
  components: {
    Rsociaux
  },
  methods: {
    passIndex(index) {
      this.$store.commit("setIndex", index);
    }
  }
};
</script>
<style lang="scss">
.footer{
  position:relative;
  top:100vh;
}
.footer-rsociaux {
  width:100%;
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
