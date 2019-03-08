<template>
  <svg version="1.1" viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet">
    <g>
      <circle cx="250" cy="250" r="200"></circle>
      <foreignObject x="10%" y="10%" width="80%" height="80%">
        <div
          class="container-circle-half"
          id="background-circle"
          :style="`background-image: url(${dataCercle.toImage})`"
        ></div>
        <div class="container-circle-half">
          <div class="columns is-mobile is-multiline">
            <div class="column is-12">
              <p>{{dataCercle.toTitle}}</p>
            </div>
            <div class="column is-12">
              <slot></slot>
            </div>
          </div>
        </div>
      </foreignObject>
    </g>
  </svg>
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
svg {
  max-width: 640px;
  max-height: 640px;
}
circle {
  fill: white;
  -webkit-filter: drop-shadow(0 0 15px rgba(0, 0, 0, 0.4));
  filter: drop-shadow(0 0 15px rgba(0, 0, 0, 0.4));
}
foreignObject {
  border-radius: 50%;
}
.container-circle-half {
  min-width: 100%;
  min-height: 50%;
}
#background-circle {
  background-repeat: no-repeat;
  background-position: center;
}
</style>