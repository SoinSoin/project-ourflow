<template>
  <div class="swiper-container">
    <div class="swiper-wrapper">
      <slot></slot>
    </div>
    <div class="swiper-button-next has-text-grey-dark"></div>
    <div class="swiper-button-prev has-text-grey-dark"></div>
  </div>
</template>

<script>
import Swiper from "swiper/dist/js/swiper.esm.bundle";
export default {
  name: "Slider",
  props: {
    slides: Array
  },
  data() {
    return {
      changeSlide: null,
      virtualData: {
        slides: []
      }
    };
  },
  mounted() {
    this.initSlide();
  },
  computed: {
    getStoreIndex() {
      return this.$store.getters.getIndex;
    }
  },
  watch: {
    getStoreIndex(index) {
      console.log("store", index);
      this.changeSlide.slideTo(index, 500);
    }
  },

  methods: {
    initSlide() {
      const self = this;
      const swiper = new Swiper(".swiper-container", {
        initialSlide: this.$store.getters.getIndex,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        },
        virtual: {
          slides: self.slides,
          renderExternal(data) {
            self.$store.commit("updateIindexNavSlide", this.realIndex);
            console.log(data.offset)
            self.$store.commit('updateSizeSlider', data.offset)
            self.virtualData = data;
            self.changeSlide = this;
            if (this.realIndex > 0) {
              self.$router.push({
                name: "contents",
                params: {
                  page: self.slides[this.realIndex].toLowerCase()
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
    }
  }
};
</script>

<style lang="scss">
.swiper-button-prev {
  background-image: url("/img/left-arrow.svg") !important;
}
.swiper-button-next {
  background-image: url("/img/right-arrow.svg") !important;
}
.resp-nav-slide {
  border-radius: 50% !important;
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
}
</style>