<template>
  <div class="container-icons">
    <div class="columns is-8 is-mobile">
      <div class="column is-fullcentered">
        <a class="icon" href="https://facebook.com/ourflowagenceweb/">
          <fa-icon class="rs" :icon="{ prefix: 'fab', iconName: 'facebook-f' }" size="2x"/>
        </a>
      </div>
      <div class="column is-fullcentered">
        <a class="icon" href="https://instagram.com/ourflowagenceweb/">
          <fa-icon class="rs" :icon="{ prefix: 'fab', iconName: 'instagram' }" size="2x"/>
        </a>
      </div>
      <div class="column is-fullcentered">
        <a class="icon" href="https://twitter.com/flow_our/">
          <fa-icon class="rs" :icon="{ prefix: 'fab', iconName: 'twitter' }" size="2x"/>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RSociaux"
};
</script>

<style lang="scss">
.container-icons {
  min-width: 25%;
}
.rs {
  color: #262524;
  transition-duration: 0.3s;
}

@media screen and (min-width: 1024px) {
  .rs:hover {
    color: rgba(38, 37, 36, 0.8);
  }
}
@media screen and (max-width: 1023px) {
  .rs {
    color: #ffffff;
  }
  .rs:focus {
    color: rgba(255, 255, 255, 0.8);
  }
}
</style>