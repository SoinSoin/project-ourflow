<template>
  <div class="size-content">
    <div class="container-card-content">
      <div class="top-content-card">
        <div class="card-content has-text-left has-text-centered-mobile">
          <div class="media">
            <div class="media-content">
              <p class="title is-4 has-text-warning">{{dataCard.title}}</p>
            </div>
          </div>
          <div class="content">{{dataCard.text}}</div>
        </div>
      </div>
      <div class="bottom-content-card"></div>
      <!-- <a class="button is-danger is-outlined is-rounded">{{valueBtn}}</a> -->
    </div>
  </div>
</template>
<script>
export default {
  name: "TextCard",
  props: {
    dataCard: Object
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
    height: 35%;
    width: 100%;
    background: yellow;
  }
  .top-content-card {
    overflow: auto;
    height: 65%;
    width: 100%;
  }
}

@media screen and (max-width: 769px) {
  .container-card-content {
    height: 50%;
    width: 100%;
  }
}
</style>

