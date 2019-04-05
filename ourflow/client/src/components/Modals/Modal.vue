<template>
  <article id="main-modal" class="columns is-gapless">
    <div class="column is-6 stencil-modal has-background-warning">
      <div class="hero is-fullheight hero-fullheight">
        <div class="hero-body">
          <div class="content-modal">
            <div class="content-top"></div>
            <div class="content-bottom ">
              <slot/>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-6 has-background-white content-modal">
      <!-- <div class="container-content-modal"></div> -->
      <div class="hero is-fullheight hero-fullheight">
        <div class="hero-body"></div>
      </div>
    </div>
  </article>
</template>
<script>
export default {
  name: "Modal",
  props: {
    dataModal: Object
  }
};
</script>
<style lang="scss">
#main-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 35;
}
.hero-fullheight{
    min-height: 0 !important;
    height:100vh;
}
#main-modal:before {
  content: "";
  position: absolute;
  background-image: url("/img/vague_carte_portfolio.svg");
  background-size: contain;
  background-repeat: no-repeat;
  top: -1%;
  height: 102%;
  transform: rotate(180deg);
  left: 5%;
  width: 50%;
}
.content-modal {
  height: 100%;
  width:100%;
}
.container-content-modal {
  height: 100%;
  padding: 5% 10%;
}
.content-top {
  height: 80%;
}
.content-bottom {
  height: 20%;
}
@media screen and (max-width: 769px) {
  .content-modal {
    height: 50%;
  }
}
</style>


