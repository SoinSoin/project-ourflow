<template>
  <div id="main-skeleton">
    <section id="main-slider" class="hero is-fullheight">
      <Slider class="hero-body">
        <Slide v-for="(content, index) in $store.getters.getDataSlide" :key="index">
          <Cercle :dataCercle="content">
            <span class="action" @click="smoothDown">
              <Btn :valueBtn="'voir'" :hasType="'slide'"/>
            </span>
          </Cercle>
        </Slide>
      </Slider>
    </section>
    <router-view/>
  </div>
</template>

<script>
import Slider from "@/components/Sliders/Slider.vue";
import Btn from "@/components/Btns/Btn.vue";
import Cercle from "@/components/Cercles/Cercle.vue";
import Slide from "@/components/Sliders/Slide.vue";

export default {
  name: "Skeleton",
  components: {
    Slider,
    Slide,
    Btn,
    Cercle
  },
  beforeMount() {
    this.getIndexSlideInit();
  },
  methods: {
    getIndexSlideInit() {
      var targetIndexRoute = this.$store.getters.getPage.indexOf(
        this.$route.params.page
      );
      // rend l'index de home comme dans l'url home ="" on peut pas savoir.
      if (this.$route.params.page === undefined) targetIndexRoute = 0;
      this.$store.commit("updateIindexNavSlide", targetIndexRoute);
    },
    smoothDown() {
      window.scroll({
        top: document.getElementById("main-pages").offsetTop,
        left: 0,
        behavior: "smooth"
      });
    }
  }
};
</script>
<style lang="scss" >
.hero {
  .swiper-container {
    margin: 0 0;
  }
}
#main-slider {
  position: sticky;
  top: 0;
  background-image: url("/img/bg-slide/vague_fond.png"),
    url("/img/bg-slide/background_desktop.png");
  background-size: 140%, cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed, fixed;
}
@media screen and (max-width: 767px) {
  #main-slider {
    background-image: url("/img/bg-slide/vague_fond.png"),
      url("/img/bg-slide/background_tablette.png");
    background-size: 150%, cover;
  }
}
</style>


