<template>
  <div id="main-portfolio" class="container">
    <Card v-for="(val, index) in obj" :key="index" :isToRight="index" :fetchDataCard="val"/>
  </div>
</template>
<script>
import Card from "@/components/Cards/Card.vue";
export default {
  name: "Portfolio",
  components: {
    Card
  },
  data() {
    return {
      obj: [
        {
          img: "https://bulma.io/images/placeholders/1280x960.png",
          title: "TITLE",
          text:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas lacinia enim ut massa pharetra, non mattis dolor feugiat."
        },
        {
          img: "https://bulma.io/images/placeholders/1280x960.png",
          title: "TITLE",
          text:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas lacinia enim ut massa pharetra, non mattis dolor feugiat."
        }
      ],
    };
  }
};
</script>

