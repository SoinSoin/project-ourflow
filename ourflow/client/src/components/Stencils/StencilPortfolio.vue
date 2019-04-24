<template>
  <svg
    class="main-stencil-portfolio"
    version="1.1"
    id="Calque_1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    x="0px"
    y="0px"
    viewBox="0 0 122 510"
    style="enable-background:new 0 0 122 510;"
    xml:space="preserve"
    v-if="$store.getters.getSize > 767"
  >
    <path
      d="M0,510.4h96.6C76.8,477.1,75.2,436.2,77,398.5c5.7-117.2,48.3-229.9,44.7-347.9c-0.1-3-1.3-38.9-5.6-50.6H0
	V510.4z"
    ></path>
  </svg>
  <svg
    class="main-stencil-portfolio"
    version="1.1"
    id="Calque_1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    x="0px"
    y="0px"
    viewBox="0 0 510 122"
    style="enable-background:new 0 0 510 122 ;"
    xml:space="preserve"
    v-else
  >
    <path
      class="st0"
      d="M0,510.4h96.6C76.8,477.1,75.2,436.2,77,398.5c5.7-117.2,48.3-229.9,44.7-347.9c-0.1-3-1.3-38.9-5.6-50.6H0
	V510.4z"
      transform="translate(510, 0) rotate(90)"
    ></path>
  </svg>
</template>
<script>
export default {
  name: "StencilPortfolio"
};
</script>

