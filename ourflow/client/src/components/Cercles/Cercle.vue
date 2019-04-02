<template>
  <div class="container-circle container">
    <div class="circle is-fullcentered">
      <article class="content-circle">
        <figure
          class="container-circle-half background-circle"
          :style="{'background-image':`url(${dataCercle.item[0].media_item})`}"
          :alt="`${dataCercle.item[0].alt_item}`"
        >
          <h1 class="title is-1 has-text-white to-bottom-text">{{dataCercle.title_para}}</h1>
        </figure>
        <div class="container-circle-half">
          <div class="padding-bottom-circle">
            <div class="content-text-circle">
              <div class="content is-medium has-text-centered has-text-grey-dark">
                <p class="is-size-7-mobile">{{dataCercle.item[0].descritpion_item}}</p>
              </div>
            </div>
            <div class="content-btn-circle">
              <slot/>
            </div>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: "Cercle",
  props: {
    dataCercle: {}
  }
};
</script>

<style lang="scss">
.circle {
  width: 100%;
  height: 100%;
}
.circle:after {
  content: "";
  display: block;
  width: 45%;
  padding-bottom: 45%;
  background-color: white;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
  border-radius: 50%;
}
.content-circle {
  position: absolute;
  height: 100%;
  width: 45%;
  border-radius: 50%;
  overflow: hidden;
  .container-circle-half {
    width: 100%;
    height: 50%;
    position: relative;
  }
}
.background-circle {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  // filter: grayscale(80%);
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.padding-bottom-circle {
  padding: 1.8em !important;
  height: 60%;
  .content-btn-circle {
    padding: 0.8em;
    height: 30%;
  }
  .content-text-circle {
    padding: 0.8em;
    height: 70%;
    overflow: auto;
  }
}
.to-bottom-text {
  line-height: 0.6 !important;
}

@media screen and (min-width: 768px) and (max-width: 1024px) {
  .circle:after {
    width: 65%;
    padding-bottom: 65%;
  }
  .content-circle {
    width: 65%;
  }
  .padding-bottom-circle {
    padding: 1.2em !important;
    .content-btn-circle {
      padding: 0.6em;
    }
    .content-text-circle {
      padding: 0.6em;
    }
  }
}

@media screen and (max-width: 767px) and (orientation: portrait) {
  .circle:after {
    width: 80%;
    padding-bottom: 80%;
  }
  .content-circle {
    width: 80%;
  }
  .padding-bottom-circle {
    padding: 0.6em !important;
    .content-btn-circle {
      padding: 0.3em;
    }
    .content-text-circle {
      padding: 0.3em;
    }
  }
}

@media screen and (max-width: 767px) and (orientation: landscape)   {
  .circle:after {
    width: 40%;
    padding-bottom: 40%;
  }
  .content-circle {
    width: 40%;
  }
  .padding-bottom-circle {
    padding: 1em !important;
    .content-btn-circle {
      padding: 0.3em;
    }
    .content-text-circle {
      padding: 0.3em;
    }
  }
}


@media screen and (min-aspect-ratio: 18/9) {
  .circle:after {
    width: 40%;
    padding-bottom: 40%;
  }
  .content-circle {
    width: 40%;
  }
  .padding-bottom-circle {
    padding: 1em !important;
    .content-btn-circle {
      padding: 0.3em;
    }
    .content-text-circle {
      padding: 0.3em;
    }
  }
}
</style>