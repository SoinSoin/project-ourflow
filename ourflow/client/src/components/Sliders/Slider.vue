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
      selfSlider: null,
      virtualData: {
        slides: []
      }
    };
  },
  mounted() {
    this.initSlide();
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
      if (this.$store.getters.getSize >= 1024) var timeAnime = 500;
      else var timeAnime = 0;
      this.selfSlider.slideTo(index, timeAnime);
    }
  },

  methods: {
    initSlide() {
      const self = this;
      const swiper = new Swiper(".swiper-container", {
        initialSlide: this.$store.getters.getIndex,
        centeredSlides: true,
        centerInsufficientSlides: true,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        },
        virtual: {
          slides: self.$store.getters.getPage,
          renderExternal(data) {
            self.$store.commit("setIndex", this.realIndex);
            self.virtualData = data;
            self.selfSlider = this; 
            self.$router.push(self.$store.getters.getUrl[this.realIndex].url);
          }
        }
      });
    },
    updateNavSlide() {
      this.selfSlider.navigation.destroy();
      this.selfSlider.navigation.init();
      this.selfSlider.navigation.update();
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
    background-image: url("/img/slider/left-arrow.svg");
  }
  .swiper-button-next {
    background-image: url("/img/slider/right-arrow.svg");
  }
}
.container-swiper-nav-resp {
  position: absolute;
  height: auto;
  z-index: 5;
  top: 80vh;
  left: 0;
  width: 100%;
  padding: 0 30%;
}

@media screen and (max-width: 1024px) and (orientation: landscape) {
  .container-swiper-nav-resp {
    top: 90vh;
  }
}


</style>