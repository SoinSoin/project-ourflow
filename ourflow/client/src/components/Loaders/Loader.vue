<template>
  <div class="container is-fluid is-marginless">
    <div class="container-loader has-background-warning">
      <div class="loader-perso">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2236.55 878.01">
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
        <p class="chargement">20%</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Loader"
};
</script>
<style lang="scss">
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

.container-loader {
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
}

.vague-loader {
  width: 100px;
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
