<template>
  <div id="main-skeleton">
    <section id="main-slider" class="hero is-fullheight">
      <Slider class="hero-body">
        <Slide v-for="(content, index) in $store.getters.getDataSlide" :key="index">
          <Cercle :dataCercle="content" :isYellow="index">
            <span class="action" @click="smoothDown">
              <Btn :valueBtn="'voir'" :hasType="'slide'"/>
            </span>
          </Cercle>
        </Slide>
      </Slider>
      <Rsociaux v-if="$store.getters.getSize>=1024" class="desktop-rs"/>
    </section>
    <router-view/>
  </div>
</template>

<script>
import Slider from "@/components/Sliders/Slider.vue";
import Btn from "@/components/Btns/Btn.vue";
import Cercle from "@/components/Cercles/Cercle.vue";
import Slide from "@/components/Sliders/Slide.vue";
import Rsociaux from "@/components/RSociaux/Rsociaux.vue";

export default {
  name: "Skeleton",
  components: {
    Slider,
    Slide,
    Btn,
    Cercle,
    Rsociaux
  },
  methods: {
    smoothDown() {
      window.scrollTo({
        top: document.getElementById("main-pages").offsetTop,
        left: 0,
        behavior: "smooth"
      });
    }
  }
};
</script>
<style lang="scss" >
.desktop-rs {
  position: absolute;
  z-index: 1;
  top: 94vh;
  left: 4vw;
}
.hero {
  .swiper-container {
    margin: 0 0;
  }
}

#main-slider {
  position: relative;
  height: 100%;
  width: 100%;
  background-image: url("/img/background/bg_vague.png"),
    url("/img/background/bg_desktop.png");
  background-size: 140%, cover;
  background-position: center, center;
  background-repeat: no-repeat, no-repeat;
}
@media screen and (min-width: 1024px) {
  #main-slider {
    position: fixed !important;
    top: 0;
  }
}
@media screen and (max-width: 1024px) {
  #main-slider {
    background-image: url("/img/background/bg_vague.p ng"),
      url("/img/background/bg_tablette.png");
  }
}
@media screen and (max-width: 767px) {
  #main-slider {
    background-image: url("/img/background/bg_vague.png"),
      url("/img/background/bg_mobile.png");
    background-size: 150%, cover;
  }
}
</style>


