<template>
  <article id="main-modal">
    <div class="columns is-gapless">
      <div class="column is-one-thirds has-background-warning stencil-modal">
        <div class="hero">
          <div class="hero-body content-modal">
            <div class="content-modal-top">
              <div class="content">
                <h2>{{dataModal.title_para}}</h2>
                <p>{{dataModal.item[0].descritpion_item}}</p>
              </div>
            </div>
            <div class="content-modal-bottom">
              <slot/>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-two-thirds has-background-white content-modal">
        <div class="hero">
          <div class="hero-body content-modal">
            <div class="content-modal-image">
              <figure v-for="(item, index ) in dataModal.item" :key="index" class="img-modal">
                <img :src="item.media_item" :alt="item.alt_item">
              </figure>
            </div>
          </div>
        </div>
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
  z-index: 35;
  width: 100vw;
  height: 100vh;
  overflow: auto;
}
.content-modal {
  height: 100vh;
  .content-modal-top {
    height: 80%;
    margin: 0 0 10% 0;
    overflow: auto;
  }
  .content-modal-bottom {
    height: 10%;
  }
}
.stencil-modal {
  position: relative;
  width: 100%;
  height: 100%;
}
.stencil-modal:before {
  content: "";
  background-image: url("/img/separation_vague.svg");
  background-size: contain;
  background-repeat: no-repeat;
  position: absolute;
  overflow: hidden;
  width: 16vw;
  height: 100%;
  left: calc(100% - 5px);
  top: 0;
}

.content-modal-image {
  height: 100%;
  overflow: auto;
  .img-modal {
    margin: 1.5em auto;
    img {
      width: 80%;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
      border-radius: 10px;
    }
  }
}

@media screen and (max-width: 767px) {
  .stencil-modal:before {
    content: "";
    background-size: 102%;
    background-image: url("/img/separation_vague_mobile.svg");
    top: calc(100% - 5px);
    left: -1%;
    height: 20vh;
    width: 101%;
  }
  .content-modal {
    // overflow: auto;
    min-height: 50vh;
    height: auto;
    .content-modal-top {
      min-height: 80%;
      height: auto;
      margin: 0 0 10% 0;
    }
    .content-modal-bottom {
      min-height: 10%;
      height: auto;
    }
  }
}
</style>


