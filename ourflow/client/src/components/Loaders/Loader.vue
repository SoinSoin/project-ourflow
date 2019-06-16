<template>
  <div id="loading" class="hero is-fullheight has-background-warning">
    <div class="hero-body">
      <div class="container">
        <div class="loader-perso columns is-multiline is-gapless">
          <div class="column is-12 is-fullcentered" style="margin: 0.25em 0;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2236.55 878.01" height="15px">
              <title>Fichier 2</title>
              <g id="Calque_2" data-name="Calque 2">
                <g id="Calque_2-2" data-name="Calque 2">
                  <path
                    class="cls-1"
                    d="M175,703,649.53,402.09a330.87,330.87,0,0,1,323.86-12.15l240.15,123.29a378.28,378.28,0,0,0,377.92-18.71L2061.55,175"
                  ></path>
                </g>
              </g>
            </svg>
          </div>
          <div class="column is-12 is-fullcentered" style="margin: 0.25em 0;">
            <slot/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Loader",
  beforeCreate() {
    document.title = `OurFlow | loading...`;
  },
  mounted() {
    this.containerIsActive();
  },
  destroyed() {
    this.containerIsActive();
  },
  methods: {
    containerIsActive(bool) {
      // pass the html to overflow hidden
      document.documentElement.classList.toggle("is-clipped");
    }
  }
};
</script>
<style lang="scss">
#loading {
  max-width: 100vw !important;
}
.cls-1 {
  fill: none;
  stroke: #fff;
  stroke-linecap: round;
  stroke-miterlimit: 10;
  stroke-width: 350px;
  stroke-dasharray: 2500;
  stroke-dashoffset: -2500;
  animation: dash 1.2s linear infinite;
  transform: scale(1);
}

@keyframes dash {
  0% {
    stroke-dashoffset: 2500;
  }

  50% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: -2500;
  }
}

.vague-loader {
  width: 100px;
  height: auto;
  animation-name: gigotementVague;
  animation-duration: 1s;
  animation-iteration-count: infinite;
  animation-timing-function: cubic-bezier(0.23, 0.44, 0.75, 0.07);
}

.chargement {
  font-family: "Montserrat";
  font-weight: 700;
  font-size: 0.8em;
  color: #fff;
}

.loader-perso {
  transform: scale(2);
}

@keyframes gigotementVague {
  0% {
    transform: rotate(0deg);
  }

  5% {
    transform: rotate(-30deg);
  }

  10% {
    transform: rotate(40deg);
  }

  15% {
    transform: rotate(-10deg);
  }

  20% {
    transform: rotate(10deg);
  }

  25% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(0deg);
  }
}
</style>
