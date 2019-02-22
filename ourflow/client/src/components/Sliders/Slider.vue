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
  props: {
    targetIndex: Number,
    slides: Array
  },
  data() {
    return {
      isClick: false,
      changeSlide: null
    };
  },
  mounted() {
    this.initSlide();
  },
  watch: {
    targetIndex: function(thisIndex) {
      if (thisIndex !== null) this.changeSlide.slideTo(thisIndex, 500);
    }
  },
  methods: {
    initSlide() {
      const self = this;
      const swiper = new Swiper(".swiper-container", {
        initialSlide: this.targetIndex,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        },
        virtual: {
          slides: self.slides,
          renderExternal(data) {
            if (this.realIndex !== 0) {
              self.$router.push({
                name: "contents",
                params: { page: self.slides[this.realIndex] }
              });
            } else {
              self.$router.push({
                name: "home"
              });
            }
            console.log("pass event slide");
            self.changeSlide = this;
          }
        }
      });
    }
  }
};
</script>

