<template>
    <div class="rond">
        {{dataCercle.toTitle}}
        <img :src="dataCercle.toImage">
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
.rond {
    height: 85vh;
    width: 85vh;
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
    text-align: center;
    
}
</style>