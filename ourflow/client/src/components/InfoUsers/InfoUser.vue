<template>
  <article class="message is-success">
    <div class="message-header">
      <figure class="image is-48x48">
        <img class="is-rounded" :src="dataToComponent.avatar_url">
      </figure>
      <p>{{dataToComponent.login}}</p>
    </div>
    <div class="message-body">
      <div class="columns is-multiline">
          <div class="column is-12">
              <p class="subtitle is-5">id: {{dataToComponent.id}}</p> 
          </div>
          <div class="column is-12">
              <p class="subtitle is-5">followers: {{dataToComponent.followers}}</p> 
          </div>          
      </div>
    </div>
  </article>
</template>

<script>
export default {
    name: "infouser",
    props:{
        dataToComponent: {}
    }
}
</script>
