<template>
  <div :id="`main-${$store.getters.getPage[$store.getters.getIndex]}`">
    <Section :hasColor="0">
      <div class="columns is-gapless">
        <div class="column is-half">
          <div class="container-colonne-gauche">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
            <div class="info-contact">
              <div class="info-contact-1">
                <img src="img/contact_mail.png">
                <p>contact@ourflow.fr</p>
              </div>
              <div class="info-contact-1">
                <img src="img/contact_telephone.png">
                <p>01 23 45 67 89</p>
              </div>
              <div class="info-contact-1">
                <img src="img/contact_adresse.png">
                <p>
                  3 rue de blablabla
                  <br>09100 Pamiers
                </p>
              </div>
            </div>
          </div>
        </div>

        <div class="column is-half">
          <div class="container-colonne-droite">
            <form class="columns is-multiline" onsubmit="return false">
              <div class="column is-12">
                <div class="field">
                  <div class="control">
                    <input class="input" type="text" placeholder="Name">
                  </div>
                </div>
              </div>

              <div class="column is-12">
                <div class="field">
                  <div class="control">
                    <input class="input" type="email" placeholder="Email">
                  </div>
                </div>
              </div>

              <div class="column is-12">
                <div class="field">
                  <div class="control">
                    <input class="input" type="tel" placeholder="Telephone">
                  </div>
                </div>
              </div>

              <div class="column is-12">
                <div class="field">
                  <div class="control">
                    <textarea class="textarea has-fixed-size" placeholder="Message"></textarea>
                  </div>
                </div>
              </div>

              <div class="column is-12">
                <div class="field btn-envoyer-container">
                  <div class="control">
                    <button class="button is-link btn-envoyer" id="message-is-send">Envoyer</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </Section>
    <!-- http://animista.net/play/basic/flip/flip-horizontal-top -->
  </div>
</template>
<script>
import Section from "@/components/Sections/Section.vue";
export default {
  name: "Contact",
  components: {
    Section
  }
};
</script>
<style lang="scss">
.container-colonne-gauche,
.container-colonne-droite {
  padding: 50px;
}

.info-contact {
  padding-left: 20px;
}
.info-contact > div {
  display: flex;
  align-items: center;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  margin: 20px 0;
}

.container-colonne-gauche > p {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  margin: 0 0 0 20px;
}

.info-contact > div img {
  margin-right: 30px;
}

form {
  text-align: center;
}

.container-colonne-droite input,
.container-colonne-droite textarea {
  border-radius: 0;
  box-shadow: none;
  border-width: 0;
  border-bottom-width: 0px;
  border-bottom: solid 2px #e2d637;
  transition-duration: 0.3s;
  background-color: transparent;
  position: relative;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
}

.input:active,
.input:focus,
.textarea:active,
.textarea:focus {
  box-shadow: none;
  border-bottom: solid 2px #c9c9c9;
  width: 100%;
}

.container-colonne-droite .btn-envoyer,
.container-colonne-droite .btn-envoyer.is-link {
  background-color: #fff;
  border: solid 2px #e2d637;
  color: #e2d637;
  transition-duration: 0.3s;
  border-radius: 50px;
  padding-left: 30px;
  padding-right: 30px;
}


.container-colonne-droite .btn-envoyer:active {
  opacity: 0.6;
}

.container-colonne-droite {
  button {
    &.button {
      &.btn-envoyer:hover {
        background-color: #e2d637;
        color: #fff;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
      }
    }
  }
}

.btn-envoyer-container {
  display: flex;
  justify-content: center;
}

.container-colonne-droite .btn-envoyer.message-send {
  background-color: greenyellow;
  border-color: greenyellow;
  transition-duration: 0.5s;
  color: #fff;
}

@media (max-width: 768px) {
  .container-colonne-droite {
    padding-top: 0;
  }
}
</style>


