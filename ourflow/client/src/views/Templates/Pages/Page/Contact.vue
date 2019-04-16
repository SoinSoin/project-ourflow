<template>
  <div :id="`main-${$store.getters.getPage[$store.getters.getIndex]}`">
    <Section :hasColor="0" :titleSec="$store.getters.getPage[$store.getters.getIndex] " :hasStencil="true">
      <div class="columns is-gapless">
        <div class="column is-half">
          <div class="container-colonne-gauche">
            <div class="columns is-8 is-multiline">
              <div class="column is-12" v-for="(objChild, i) in fetchData.paragraph" :key="i">
                <div class="content has-text-left has-text-centered-mobile">
                  <p class="title is-6">{{objChild.item[0].descritpion_item}}</p>
                </div>
              </div>
            </div>
            <Coordinate/>
          </div>
        </div>
        <div class="column is-half">
          <div class="container-colonne-droite">
            <form class="columns is-multiline" onsubmit="return false">
              <div class="column is-12">
                <div class="field">
                  <p class="control has-icons-left has-icons-right">
                    <input
                      :class="{'input':true, 'input-mail':true, 'is-normal-higlight': this.is.name.color==='normal','is-red-higlight':this.is.name.color==='red'}"
                      type="text"
                      v-model="dataForm.name"
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
                      v-model="dataForm.email"
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
                      v-model="dataForm.phone"
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
                      :class="{'input':true, 'has-fixed-size':true, 'textarea':true, 'input-mail':true, 'is-normal-higlight': this.is.message.color==='normal','is-red-higlight':this.is.message.color==='red'}"
                      placeholder="Message"
                      v-model="dataForm.content"
                      required
                    ></textarea>
                    <span class="icon is-small is-left">
                      <p class="title is-5 has-text-warning">*</p>
                    </span>
                  </p>
                </div>
              </div>
              <div class="column is-12">
                <div class="columns is-multiline">
                  <div class="column is-12">
                    <div class="field btn-envoyer-container">
                      <div class="control modify-control is-fullcentered">
                        <a
                          :class="{'button':true, 'red-circle':click.error,'green-circle':click.success, 'is-link':click.normal,'transition-btn-envoyer':true, 'btn-envoyer':click.normal, 'is-rounded':true, 'is-link-to-circle':!click.normal,}"
                        >
                          <span
                            @click="beforeSend()"
                            v-if="click.normal"
                            class="action-send is-fullcentered"
                          >
                            <p>{{msg}}</p>
                          </span>
                          <span v-else class="icon is-medium">
                            <fa-icon v-if="click.error" :icon="{prefix: 'fas', iconName:'times'}"/>
                            <fa-icon
                              v-if="click.success"
                              :icon="{prefix: 'fas', iconName:'check'}"
                            />
                          </span>
                        </a>
                      </div>
                    </div>
                  </div>
                  <div class="column is-12">
                    <p class="title is-6 has-text-danger has-text-centered">{{error}}</p>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </Section>
  </div>
</template>
<script>
import Section from "@/components/Sections/Section.vue";
import Coordinate from "@/components/Coordinates/Coordinate";
import setMail from "@/services/api.js";
export default {
  name: "Contact",
  components: {
    Section,
    Coordinate
  },
  props: {
    fetchData: Object
  },
  data() {
    return {
      error: "",
      msg: "Envoyer",
      click: {
        normal: true,
        error: false,
        success: false
      },
      dataForm: {
        name: "",
        email: "",
        phone: "",
        content: ""
      },
      is: {
        name: {
          color: "normal"
        },
        mail: {
          color: "normal"
        },
        phone: {
          color: "normal"
        },
        message: {
          color: "normal"
        }
      }
    };
  },
  computed: {
    dataMail() {
      return this.dataForm.email;
    },
    dataPhone() {
      return this.dataForm.phone;
    },
    dataName() {
      return this.dataForm.name;
    },
    dataMessage() {
      return this.dataForm.content;
    }
  },
  watch: {
    dataMessage() {
      this.is.message.color = "normal";
    },
    dataName() {
      this.is.name.color = "normal";
    },
    dataMail(mail) {
      // verif if a string is a mail type
      if (mail !== "") {
        if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) {
          this.is.mail.validate = true;
          this.is.mail.color = "green";
        } else {
          this.is.mail.validate = false;
          this.is.mail.color = "red";
        }
      } else {
        this.is.mail.validate = false;
        this.is.mail.color = "normal";
      }
    },
    dataPhone(phone) {
      // verif if a phone number
      if (phone !== "") {
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
      } else {
        this.is.phone.validate = true;
        this.is.phone.color = "normal";
      }
    }
  },
  methods: {
    beforeSend() {
      var dataForm = new FormData();
      for (var attrData in this.dataForm) {
        dataForm.set(attrData, this.dataForm[attrData]);
      }
      this.sendMail(dataForm);
    },
    isSuccess() {
      this.click.normal = false;
      this.click.success = true;
      this.returnIsNormal();
      this.emptyForm();
    },
    isError(dataErr) {
      this.click.normal = false;
      this.click.error = true;
      this.error = dataErr.msg;
      this.is[dataErr.from].color = "red";
      this.returnIsNormal();
    },
    returnIsNormal() {
      const toNormal = setInterval(() => {
        this.click.normal = true;
        this.click.success = false;
        this.click.error = false;
        clearInterval(toNormal);
      }, 3000);
    },
    sendMail(dataForm) {
      setMail
        .setSendMail(dataForm)
        .then(res => {
          this.isSuccess();
        })
        .catch(error => {
          this.isError(error.response.data);
        });
    },
    emptyForm() {
      for (var attrDataForm in this.dataForm) {
        this.dataForm[attrDataForm] = "";
      }
      this.error = "";
    }
  }
};
</script>
<style lang="scss">
.modify-control {
  width: 100% !important;
  min-height: 4vh !important;
}
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
      border-bottom: solid 2px hsl(141, 71%, 48%);
    }
    &.is-red-higlight {
      border-bottom: solid 2px #ff5b28;
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
      border-bottom: solid 2px hsl(141, 71%, 48%);
    }
    &.is-red-higlight {
      border-bottom: solid 2px #ff5b28;
    }
    width: 100%;
  }
}

.container-colonne-droite .btn-envoyer,
.container-colonne-droite .btn-envoyer.is-link {
  background-color: #fff;
  border: solid 2px #e2d637;
  color: #e2d637;
  padding: 0 30px;
  height: 40px;
  // border-radius: 50px;
}
.transition-btn-envoyer {
  transition-duration: 0.3s !important;
}

.action-send {
  height: 100%;
  padding: 14% 0;
}

.is-link-to-circle {
  height: 40px !important;
  width: 40px !important;
  border: none !important;
}

.red-circle {
  background: #ff5b28 !important;
  color: white !important;
}
.green-circle {
  background: hsl(141, 71%, 48%) !important;
  color: white !important;
}
.container-colonne-droite .btn-envoyer:active {
  opacity: 0.6;
}

.container-colonne-droite .btn-envoyer.is-link:hover {
  background-color: #e2d637;
  color: #fff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
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

@media (max-width: 767px) {
  .container-colonne-gauche,
  .container-colonne-droite {
    padding: 50px 0;
  }
}
</style>


