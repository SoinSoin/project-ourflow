<template>
  <div class="card">
    <div class="columns">
      <div class="column is-one">
        <div class="card-image">
          <figure class="image is-4by3">
            <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
          </figure>
        </div>
      </div>
      <div class="column">
        <div class="card-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">{{valueTitle}}</p>
            </div>
          </div>
          <div class="content">{{valueText}}</div>
          <!-- <a class="button is-danger is-outlined is-rounded">{{valueBtn}}</a> -->
        </div>
      </div>
    </div>
  </div>
</template>
​
<script>
export default {
  props: {
    valueTitle: String,
    valueText: String
    // valueBtn: String
  }
};
</script>

<style lang="scss">
.card {
  width: 40%;
  margin-left: 30%;
  box-shadow : 0 10px 50px rgba(0, 0, 0, 0.3) !important;
}

.card-content {
  padding: 0% !important;
  text-align: left;
}

.is-one {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

.title {
    color: #ffdb2b !important;
}

</style>