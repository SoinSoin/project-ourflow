<template>
  <div class="container is-fullhd">
    <section id="main-slider">
      <Slider
        :indexToSlider="passIndexSliderToSkeleton"
        :slides="sendArraySlider"
        @indexFromSlide="passSlideToSkeleton"
      >
        <Slide v-for="(content, index) in dataMainSlider" :key="index">
          <p>{{content.name}}</p>
        </Slide>
      </Slider>
      <Card :valueTitle="'TITLE'" :valueText="'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas lacinia enim ut massa pharetra, non mattis dolor feugiat.'"/>
    </section>
    <router-view/>
  </div>
</template>

<script>
import Card from "@/components/Cards/Card.vue";
import Slider from "@/components/Sliders/Slider.vue";
import Slide from "@/components/Sliders/Slide.vue";
export default {
  name: "Skeleton",
  components: {
    Slider,
    Slide,
    Card
  },
  data() {
    return {
      dataMainSlider: [],
      sendArraySlider: [],
      passIndexSliderToSkeleton: Number
    };
  },
  props: {
    indexToSkeleton: Number
  },
  beforeMount() {
    this.getDataPagesSlider();
  },

  watch: {
    indexToSkeleton(index) {
      this.passIndexSliderToSkeleton = index;
    },
    passIndexSliderToSkeleton(index) {
      this.returnTobodyIndex(index);
    }
  },
  methods: {
    getDataPagesSlider() {
      var objData = [
        { name: "Accueil", linkto: "home" },
        { name: "Prestation", linkto: "prestation" },
        { name: "Contact", linkto: "contact" }
      ];
      this.dataMainSlider = objData;
      objData.map(pageLink => {
        this.sendArraySlider.push(pageLink.linkto);
      });
      this.getIndexSlideInit();
    },
    getIndexSlideInit() {
      this.passIndexSliderToSkeleton = this.sendArraySlider.indexOf(
        this.$route.params.page
      );
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

