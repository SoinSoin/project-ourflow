<template>
  <div id="main-skeleton">
    <section id="main-slider" class="hero is-fullheight">
      <Slider class="hero-body" v-if="sendArraySlider.length" :slides="sendArraySlider">
        <Slide v-for="(content, index) in $store.getters.getDataSlide" :key="index">
          <Cercle :dataCercle="content">
            <Btn :valueBtn="'voir'" :hasType="content.type.toLowerCase()"/>
          </Cercle>
        </Slide>
      </Slider>
    </section>
    <router-view/>
  </div>
  <!-- <Btn :valueBtn="'DÉCOUVRIR'"/> -->
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
  data() {
    return {
      sendArraySlider: [],
      sizeSlide: Number,
      targetSize: {
        width: Number,
        height: Number
      }
    };
  },
  props: {
    dataToSkeleton: Array
  },

  computed: {
    getStoreSize() {
      return this.$store.getters.getSize;
    }
  },
  watch: {
    getStoreSize(size) {
      return size;
    }
  },

  beforeMount() {
    this.getDataPagesSlider();
  },
  mounted() {
    console.log(this.$store.getters.getDataSlide);
    console.log(this.$store.getters.getData);
    this.targetSize.height = window.outerHeight;
    this.targetSize.width = window.outerWidth;
  },
  methods: {
    getDataPagesSlider() {
      this.dataToSkeleton.map(pageLink => {
        this.sendArraySlider.push(pageLink.title_page.toLowerCase());
      });
      this.getIndexSlideInit();
    },

    getIndexSlideInit() {
      var targetIndexRoute = this.sendArraySlider.indexOf(
        this.$route.params.page
      );
      // rend l'index de home comme dans l'url home ="" on peut pas savoir.
      if (this.$route.params.page === undefined) targetIndexRoute = 0;
      this.$store.commit("updateIindexNavSlide", targetIndexRoute);
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
</style>


