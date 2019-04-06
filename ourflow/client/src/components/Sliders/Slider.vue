<template>
  <div class="swiper-container">
    <div class="swiper-wrapper">
      <slot></slot>
    </div>
    <div v-if="$store.getters.getSize < 768" class="container-swiper-nav-resp">
      <div class="resp-nav-slide">
        <div class="columns is-mobile">
          <div class="icon-slide column is-4 is-fullcentered">
            <div class="swiper-button-prev resp-button"></div>
          </div>
          <div class="column is-4 has-text-centered is-fullcentered is-paddingless">
            <p class="title is-size-6-mobile has-text-grey-dark">Swipe</p>
          </div>
          <div class="icon-slide column is-4 is-fullcentered">
            <div class="swiper-button-next resp-button"></div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="icon-slide">
      <div class="swiper-button-next has-text-grey-dark"></div>
      <div class="swiper-button-prev has-text-grey-dark"></div>
    </div>
  </div>
</template>

<script>
import Swiper from "swiper/dist/js/swiper.esm.bundle";
export default {
  name: "Slider",
  data() {
    return {
      size: Number,
      changeSlide: null,
      virtualData: {
        slides: []
      }
    };
  },
  mounted() {
    this.initSlide();
    this.size = this.changeSlide.size;
  },
  updated() {
    this.updateNavSlide();
  },
  computed: {
    getStoreIndex() {
      return this.$store.getters.getIndex;
    }
  },
  watch: {
    getStoreIndex(index) {
      if (this.$store.getters.getSize > 1024) var timeAnime = 500;
      else var timeAnime = 0;
      this.changeSlide.slideTo(index, timeAnime);
    }
  },

  methods: {
    initSlide() {
      const self = this;
      const swiper = new Swiper(".swiper-container", {
        initialSlide: this.$store.getters.getIndex,
        centeredSlides: true,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        },
        virtual: {
          slides: self.$store.getters.getPage,
          renderExternal(data) {
            self.$store.commit("updateIindexNavSlide", this.realIndex);
            self.virtualData = data;
            self.changeSlide = this;
            if (this.realIndex > 0) {
              self.$router.push({
                name: "contents",
                params: {
                  page: self.$store.getters.getPage[this.realIndex]
                }
              });
            } else {
              self.$router.push({
                name: "home"
              });
            }
          }
        }
      });
    },
    updateNavSlide() {
      this.changeSlide.navigation.destroy();
      this.changeSlide.navigation.init();
      this.changeSlide.navigation.update();
    }
  }
};
</script>

<style lang="scss">
.resp-nav-slide {
  background: white;
  border-radius: 290486px;
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
}
.icon-slide {
  .resp-button {
    position: relative;
    height: 40px;
    width: 20px;
    margin-top: -20px;
    background-size: 20px 40px;
  }
  .swiper-button-prev {
    background-image: url("/img/left-arrow.svg");
  }
  .swiper-button-next {
    background-image: url("/img/right-arrow.svg");
  }
}
.container-swiper-nav-resp {
  position: absolute;
  height: auto;
  z-index: 5;
  top: 85%;
  left: 0;
  width: 100%;
  padding: 0 30%;
}
</style>