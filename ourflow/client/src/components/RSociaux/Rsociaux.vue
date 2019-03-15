<template>
  <div>
    <fa-icon class="rs" :icon="{ prefix: 'fab', iconName: 'facebook-f' }" size="2x"/>&nbsp;
    <fa-icon class="rs" :icon="{ prefix: 'fab', iconName: 'instagram' }" size="2x"/>&nbsp;
    <fa-icon class="rs" :icon="{ prefix: 'fab', iconName: 'twitter' }" size="2x"/>
  </div>
</template>

<script>
export default {
  name: "RSociaux"
};
</script>

<style lang="scss">
.rs {
  margin: 1%;
  color: black;
}
</style>