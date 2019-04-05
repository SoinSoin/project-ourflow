<template>
  <div id="main-portfolio" class="container">
    <Card
      v-for="(val, index) in fetchData.paragraph"
      :key="index"
      :isToRight="index"
      :fetchDataCard="val"
    >
      <span class="action" @click="activeModal({isModalActive:true,dataModal:val})">
        <Btn :valueBtn="'voir'"/>
      </span>
    </Card>
    <transition name="modal">
      <Modal v-if="isActiveModal">
        <span class="action" @click="closeModal(false)">
          <Btn :valueBtn="'fermer'"/>
        </span>
      </Modal>
    </transition>
  </div>
</template>
<script>
import Card from "@/components/Cards/Card.vue";
import Btn from "@/components/Btns/Btn.vue";
import Modal from "@/components/Modals/Modal.vue";
export default {
  name: "Portfolio",
  components: {
    Card,
    Btn,
    Modal
  },
  props: {
    fetchData: Object
  },
  data() {
    return {
      isActiveModal: false
    };
  },
  watch: {
    isActiveModal(bool) {
      document.documentElement.classList.toggle("is-clipped");
    }
  },
  methods: {
    activeModal(activeData) {
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
</style>


