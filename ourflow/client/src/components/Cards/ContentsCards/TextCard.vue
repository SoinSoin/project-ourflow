<template>
  <div class="size-content">
    <div class="container-card-content">
      <div class="top-content-card">
        <div class="card-content has-text-left has-text-centered-mobile">
          <div class="media">
            <div class="media-content">
              <h3 class="title is-3 has-text-warning">{{dataCard.title_para}}</h3>
            </div>
          </div>
          <div
            class="content is-size-7-mobile has-text-grey-dark"
          >{{dataCard.item[0].descritpion_item}}</div>
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
    const cutString = this.dataCard.item[0].descritpion_item.split(" ", 20);
    if (cutString.length >= 20) this.lessText(cutString);
  },
  methods: {
    lessText(arrText) {
      const sentence = arrText.join(" ");
      this.dataCard.item[0].descritpion_item = `${sentence.toString()} ... `;
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
    background: yellow;
  }
  .top-content-card {
    overflow: auto;
    height: 75%;
    width: 100%;
    padding: 5%;
  }
}

@media screen and (max-width: 769px) {
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

