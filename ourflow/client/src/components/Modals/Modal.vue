<template>
  <article id="main-modal">
    <div class="columns is-gapless contain-section">
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
        <StencilPortfolio class="stencil-background-yellow"/>
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
import StencilPortfolio from "@/components/Stencils/StencilPortfolio.vue";
export default {
  name: "Modal",
  components: {
    StencilPortfolio
  },
  props: {
    dataModal: Object
  }
};
</script>
<style lang="scss">
.stencil-modal {
  .main-stencil-portfolio {
    position: absolute;
    height: 100%;
    width: auto;
    left: 95%;
    top: 0;
    z-index: 1;
  }
}
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

.content-modal-image {
  height: 100%;
  overflow: auto;
  padding-left: 15%;
  .img-modal {
    margin: 1.5em auto;
    img {
      width: 100%;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
      border-radius: 10px;
    }
  }
}

@media screen and (max-width: 767px) {
  .stencil-modal {
    .main-stencil-portfolio {
      height: auto;
      width: 100%;
      left: 0;
      top: calc(100% - 3px);
    }
  }
  .content-modal-image {
    height: 100%;
    overflow: auto;
    padding-left: 0;
    padding-top: 15%;
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
    }
  }
}
</style>


