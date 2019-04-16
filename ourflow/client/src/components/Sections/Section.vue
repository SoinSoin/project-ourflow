<template>
  <section
    :class="{'section':true, 'stencil-white':!isYellow, 'has-background-warning':isYellow,'stencil-yellow':isYellow,}"
  >
    <div class="container">
      <div class="content">
        <h1
          :class="{'higlight-title':true, 'subtitle':true, 'is-1':true, 'is-size-2-mobile':true, 'is-capitalized':true, 'has-text-weight-light':true,'has-text-warning':!isYellow,'has-text-white':isYellow}"
        >{{title}}</h1>
      </div>
      <slot/>
    </div>
  </section>
</template>
<script>
export default {
  name: "Section",
  props: {
    hasColor: Number,
    title: String
  },
  data() {
    return {
      isYellow: Boolean
    };
  },

  beforeMount() {
    this.yellowing();
  },
  methods: {
    yellowing() {
      if (this.hasColor % 2) this.isYellow = true;
      else this.isYellow = false;
    }
  }
};
</script>
<style lang="scss">
.section {
}
</style>

