<template>
  <article id="main-modal">
    <div class="columns is-gapless">
      <div class="column is-one-thirds has-background-warning stencil-modal">
        <div class="section content-modal">
          <div class="content-modal-top">
            <div class="content has-text-left has-text-centered-mobile has-text-grey-dark">
              <h2 class="title is-2 is-size-3-mobile is-capitalized">{{dataModal.title_para}}</h2>
              <p>{{dataModal.item[0].descritpion_item}}</p>
            </div>
          </div>
          <div class="content-modal-bottom is-fullcentered">
            <slot/>
          </div>
        </div>
      </div>
      <div class="column is-two-thirds has-background-white content-modal">
        <div class="section content-modal">
          <div class="content-modal-image">
            <div class="container is-fluid">
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
  width: 100%;
  height: 100vh;
  .content-modal-top {
    width: 100%;
    height: 80%;
    overflow: auto;
  }
  .content-modal-bottom {
    width: 100%;
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
  background-image: url("/img/stencil/sc_modal.svg");
  background-size: contain;
  background-repeat: no-repeat;
  position: absolute;
  overflow: hidden;
  width: 16vw;
  height: 100%;
  left: calc(100% - 5px);
  top: 0;
  z-index: 1;
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
    background-image: url("/img/stencil/sc_modal_mobile.svg");
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
    }
    .content-modal-bottom {
      min-height: 10%;
      height: auto;
      .action {
        position: fixed;
        top: 0;
        left: 85vw;
        margin: 2vh 2vw;
        z-index: 5;
      }
    }
    .img-modal {
      margin: 1.5em auto;
      img {
        width: 90%;
      }
    }
  }
}
</style>


