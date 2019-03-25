<template>
  <div class="container is-fullhd">
    <section id="main-slider">
      <Slider
        v-if="sendArraySlider.length" 
      >
        <Slide v-for="(content, index) in dataToSkeleton" :key="index">
          <p>{{content.title_page}}</p>
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
    };
  },
  props: {
    dataToSkeleton: Array
  },

beforeMount(){
  this.getDataPagesSlider()
},
  methods: {
    getDataPagesSlider() {
      this.dataToSkeleton.map(pageLink => {
        this.sendArraySlider.push(pageLink.title_page.toLowerCase());
      });
      this.$store.commit('updateFacticeSlide',this.sendArraySlider)
      this.getIndexSlideInit();
    },

    getIndexSlideInit() {
      var targetIndexRoute = this.sendArraySlider.indexOf(
        this.$route.params.page
      );
      // rend l'index de home comme dans l'url home ="" on peut pas savoir.
      if (this.$route.params.page === undefined)
        targetIndexRoute = 0;
      this.$store.commit('updateIindexNavSlide', targetIndexRoute)
    },
  }
};
</script>

