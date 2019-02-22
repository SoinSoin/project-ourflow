<template>
  <div class="container is-fullhd">
    <section id="main-slider">
      <Slider :targetIndex="getIndexSlider" :slides="sendArraySlider">
        <Slide v-for="(content, index) in dataMainSlider" :key="index">
          <p>{{content.name}}</p>
        </Slide>
      </Slider>
    </section>
    <router-view/>
  </div>
</template>

<script>
import Slider from "@/components/Sliders/Slider.vue";
import Slide from "@/components/Sliders/Slide.vue";
export default {
  name: "Skeleton",
  components: {
    Slider,
    Slide
  },
  data() {
    return {
      dataMainSlider: [],
      getIndexSlider: Number,
      sendArraySlider: []
    };
  },
  props: {
    indexPage: Number
  },
  beforeMount() {
    this.getDataPagesSlider();
  },
  beforeUpdate() {
    this.getIndexSlider = this.indexPage;
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
      this.getIndexSlider = this.sendArraySlider.indexOf(
        this.$route.params.page
      );
      if (this.$route.params.page === undefined) this.getIndexSlider = 0;
    }
  }
};
</script>

