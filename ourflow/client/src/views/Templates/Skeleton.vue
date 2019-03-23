<template>
  <div class="container is-fullhd">
    <section id="main-slider">
      <Slider
        v-if="dataToSkeleton.length" 
        :indexToSlider="passIndexSliderToSkeleton"
        :slides="sendArraySlider"
        @indexFromSlide="passSlideToSkeleton"
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
      passIndexSliderToSkeleton: Number
    };
  },
  props: {
    indexToSkeleton: Number,
    dataToSkeleton: Array
  },

beforeMount(){
  this.getDataPagesSlider()
},

  watch: {
    indexToSkeleton(index) {
      this.passIndexSliderToSkeleton = index;
    },
    passIndexSliderToSkeleton(index) {
      this.returnTobodyIndex(index);
    },
  },
  methods: {
    getDataPagesSlider() {
      console.log(this.dataToSkeleton)
      this.dataToSkeleton.map(pageLink => {
        this.sendArraySlider.push(pageLink.title_page.toLowerCase());
      });
      this.getIndexSlideInit();
    },

    getIndexSlideInit() {
      this.passIndexSliderToSkeleton = this.sendArraySlider.indexOf(
        this.$route.params.page
      );
      // rend l'index de home comme dans l'url home ="" on peut pas savoir.
      if (this.$route.params.page === undefined)
        this.passIndexSliderToSkeleton = 0;
      
    },

    passSlideToSkeleton(index) {
      this.passIndexSliderToSkeleton = index;
    },

    returnTobodyIndex(slideIndex, event) {
      this.$emit("returnSkeltonToBody", slideIndex);
    }
  }
};
</script>

