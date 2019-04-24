<template>
  <div class="size-content">
    <div class="container-card-content">
      <div class="top-content-card is-fullcentered">
        <div class="card-content has-text-left has-text-centered-mobile">
          <div class="media">
            <div class="media-content">
              <h2
                class="title is-2 is-size-3-mobile has-text-warning has-text-centered-mobile"
              >{{dataCard.title_para}}</h2>
            </div>
          </div>
          <div class="content is-size-7-mobile has-text-grey-dark">
            <p>{{dataCard.item[0].synopsis}}</p>
          </div>
        </div>
      </div>
      <div class="bottom-content-card">
        <slot/>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "TextCard",
  props: {
    dataCard: Object
  },
  beforeMount() {
    this.targetText();
  },
  methods: {
    lessText(arrText) {
      const sentence = arrText.join(" ");
      this.dataCard.item[0].synopsis = `${sentence.toString()} ... `;
    },
    targetText() {
      const cutString = this.dataCard.item[0].descritpion_item.split(" ");
      if (this.$store.getters.getSize <= 767) var sizeText = 10;
      else var sizeText = 20;
      if (cutString.length >= 20)
        this.lessText(
          this.dataCard.item[0].descritpion_item.split(" ", sizeText)
        );
    }
  }
};
</script>
<style lang="scss">
.size-content:after {
  content: "";
  display: block;
  padding: 40% !important;
}
.container-card-content {
  position: absolute;
  height: 100%;
  width: 50%;
  .bottom-content-card {
    height: 25%;
    width: 100%;
  }
  .top-content-card {
    overflow: auto;
    height: 75%;
    width: 100%;
    padding: 5%;
  }
}

@media screen and (max-width: 767px) {
  .container-card-content {
    .top-content-card {
      padding: 0;
    }
  }
  .container-card-content {
    height: 50%;
    width: 100%;
  }
}
</style>

