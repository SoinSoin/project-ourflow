<template>
<div id="main-portfolio">
    <Section :hasColor="0" :title="$store.getters.getPage[$store.getters.getIndex] ">
      <Card
        v-for="(val, index) in fetchData.paragraph"
        :key="index"
        :isToRight="index"
        :fetchDataCard="val"
      >
        <div
          :class="{'container-action-btn':true, 'is-btn-left': index%2==false , 'is-btn-right':index%2 }"
        >
          <span class="action" @click="activeModal({isModalActive:true,dataModal:val})">
            <Btn :valueBtn="'découvrir'"/>
          </span>
        </div>
      </Card>
      <transition name="modal">
        <Modal v-if="isActiveModal" :dataModal="dataToModal">
          <span class="action" @click="closeModal(false)">
            <Btn :valueBtn="'fermer'" :hasType="'modal'"/>
          </span>
        </Modal>
      </transition>
    </Section>
  </div>
</template>
<script>
import Card from "@/components/Cards/Card.vue";
import Btn from "@/components/Btns/Btn.vue";
import Modal from "@/components/Modals/Modal.vue";
import Section from "@/components/Sections/Section.vue";
export default {
  name: "Portfolio",
  components: {
    Card,
    Btn,
    Modal,
    Section
  },
  props: {
    fetchData: Object
  },
  data() {
    return {
      isActiveModal: false,
      dataToModal: Object
    };
  },
  watch: {
    isActiveModal(bool) {
      document.documentElement.classList.toggle("is-clipped");
    }
  },
  methods: {
    activeModal(activeData) {
      this.dataToModal = activeData.dataModal;
      this.isActiveModal = activeData.isModalActive;
    },
    closeModal(close) {
      this.isActiveModal = false;
    }
  }
};
</script>

<style lang="scss">
#main-portfolio {
  background-image: url("/img/background/bg_portfolio.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: 150%;
}
.modal-leave-active {
  -webkit-animation-name: zoomOut;
  animation-name: zoomOut;
  -webkit-animation-duration: 0.8s;
  animation-duration: 0.8s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@-webkit-keyframes zoomOut {
  0% {
    opacity: 1;
  }

  50% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }
  100% {
    opacity: 0;
  }
}
@keyframes zoomOut {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }
  100% {
    opacity: 0;
  }
}
.modal-enter-active {
  -webkit-animation-name: zoomIn;
  animation-name: zoomIn;
  -webkit-animation-duration: 0.8s;
  animation-duration: 0.8s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@-webkit-keyframes zoomIn {
  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
@keyframes zoomIn {
  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
.is-btn-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.is-btn-left {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
.container-action-btn {
  height: 100%;
  width: 80%;
  margin: 0 auto;
}
@media screen and (max-width: 767px) {
  .is-btn-right {
    justify-content: center;
  }
  .is-btn-left {
    justify-content: center;
  }
  #main-portfolio {
    background-size: cover;
  }
}
</style>


