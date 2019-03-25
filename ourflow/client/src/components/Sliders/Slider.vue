<template>
  <div class="swiper-container">
    <div class="swiper-wrapper">
      <slot></slot>
    </div>
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
  </div>
</template>

<script>
import Swiper from "swiper/dist/js/swiper.esm.bundle";
export default {
  name: "Slider",
  data() {
    return {
      changeSlide: null,
      virtualData: {
        slides: [],
        },
    };
  },
  mounted() {
    this.initSlide();
  },
  computed: {
     getStoreIndex()  {
      return this.$store.getters.getIndex
    }
  },
  watch: {
    getStoreIndex(index){
      this.changeSlide.slideTo(index, 500);
      console.log(index)
    },
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
          slides: self.$store.getters.getSlides,
          renderExternal(data) {
            self.virtualData = document.querySelectorAll("swiper-slide");
            self.$store.commit('updateIindexNavSlide', this.realIndex)
            self.changeSlide = this;
            if (this.realIndex > 0) {
              self.$router.push({
                name: "contents",
                params: { page: self.$store.getters.getSlides[this.realIndex].toLowerCase() }
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
  }
};
</script>

