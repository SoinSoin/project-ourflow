<template>
  <div class="container is-fluid is-marginless">
    <section id="main-slider">
      <Slider v-if="sendArraySlider.length" :slides="sendArraySlider">
        <Slide
          v-for="(content, index) in dataToSkeleton"
          :key="index"
          :style="{left: `${sizeSlide}px`}"
        >
          <div style="height:100%;width:100%;background:blue" class="is-fullcentered">
            <div style="height:75vw;width:75vw;">{{content.title_page}}</div>
          </div>
        </Slide>
      </Slider>
      <Btn :valueBtn="'DÉCOUVRIR'"/>
    </section>
    <router-view/>
  </div>
</template>

<script>
import Slider from "@/components/Sliders/Slider.vue";
import Btn from "@/components/Btns/Btn.vue";
import Slide from "@/components/Sliders/Slide.vue";
export default {
  name: "Skeleton",
  components: {
    Slider,
    Slide,
    Btn
  },
  data() {
    return {
      sendArraySlider: [],
      sizeSlide: Number
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
    this.sizeSlide = this.$store.getters.getSize;
    console.log(this.sizeSlide);
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

