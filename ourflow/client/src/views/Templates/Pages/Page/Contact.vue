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
                  <p class="control has-icons-left has-icons-right">
                    <input
                      class="input input-mail is-normal-higlight"
                      type="text"
                      v-model="dataName"
                      placeholder="Nom ou Entreprise"
                      required
                    >
                    <span class="icon is-small is-left">
                      <p class="title is-5 has-text-warning">*</p>
                    </span>
                  </p>
                </div>
              </div>

              <div class="column is-12">
                <div class="field">
                  <p class="control has-icons-left has-icons-right">
                    <input
                      :class="{'input':true, 'input-mail':true, 'is-normal-higlight': this.is.mail.color==='normal','is-red-higlight':this.is.mail.color==='red','is-green-higlight':this.is.mail.color==='green'}"
                      type="email"
                      v-model="dataMail"
                      placeholder="Email"
                      required
                    >
                    <span class="icon is-small is-left">
                      <p class="title is-5 has-text-warning">*</p>
                    </span>
                  </p>
                </div>
              </div>

              <div class="column is-12">
                <div class="field">
                  <p class="control has-icons-left has-icons-right">
                    <input
                      :class="{'input':true, 'input-mail':true, 'is-normal-higlight': this.is.phone.color==='normal','is-red-higlight':this.is.phone.color==='red','is-green-higlight':this.is.phone.color==='green'}"
                      type="tel"
                      v-model="dataPhone"
                      placeholder="Telephone"
                    >
                    <span class="icon is-small is-left">
                      <p class="title is-5 has-text-warning"></p>
                    </span>
                  </p>
                </div>
              </div>

              <div class="column is-12">
                <div class="field">
                  <p class="control has-icons-left has-icons-right">
                    <textarea
                      class="textarea input input-mail has-fixed-size is-normal-higlight"
                      placeholder="Message"
                      v-model="dataMessage"
                      required
                    ></textarea>
                    <span class="icon is-small is-left">
                      <p class="title is-5 has-text-warning">*</p>
                    </span>
                  </p>
                </div>
              </div>
              <div class="column is-12">
                <div class="field btn-envoyer-container">
                  <div class="control">
                    <button class="button is-link btn-envoyer">Envoyer</button>
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
  },
  data() {
    return {
      dataName: "",
      dataMail: "",
      dataPhone: "",
      dataMessage: "",
      is: {
        mail: {
          validate: false,
          color: "normal"
        },
        phone: {
          validate: true,
          color: "normal"
        }
      }
    };
  },
  watch: {
    dataMail(mail) {
      if ( /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) {
        this.is.mail.validate = true;
        this.is.mail.color = "green";
      } else {
        this.is.mail.validate = false;
        this.is.mail.color = "red";
      }
    },
    dataPhone(phone) {
      switch (phone) {
        case "":
          this.is.phone.validate = true;
          this.is.phone.color = "normal";
          break;
        default:
          if (isNaN(phone)) {
            this.is.phone.validate = false;
            this.is.phone.color = "red";
          } else {
            if (phone.split("").length === 10) {
              this.is.phone.validate = true;
              this.is.phone.color = "green";
            } else {
              this.is.phone.validate = false;
              this.is.phone.color = "red";
            }
          }
          break;
      }
      console.log(this.is.phone);
    }
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
  &.input-mail {
    border-radius: 0;
    box-shadow: none;
    border-width: 0;
    border-bottom-width: 0px;
    transition-duration: 0.3s;
    background-color: transparent;
    position: relative;
    font-family: "Montserrat", sans-serif;
    font-weight: 700;
    &.is-normal-higlight {
      border-bottom: solid 2px #e2d637;
    }
    &.is-green-higlight {
      border-bottom: solid 2px green;
    }
    &.is-red-higlight {
      border-bottom: solid 2px red;
    }
  }
}

.input:active,
.input:focus,
.textarea:active,
.textarea:focus {
  &.input-mail {
    box-shadow: none;
    &.is-normal-higlight {
      border-bottom: solid 2px #c9c9c9;
    }
    &.is-green-higlight {
      border-bottom: solid 2px green;
    }
    &.is-red-higlight {
      border-bottom: solid 2px red;
    }
    width: 100%;
  }
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


