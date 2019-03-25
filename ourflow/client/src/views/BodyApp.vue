<template>
  <div id="body-app">
    <div v-if="dataNamePages.length" id="main-body" class="container is-fluid is-marginless">
      <header class="level is-mobile is-marginless">
        <div class="level-left">
          <div class="level-item">ourflow</div>
        </div>
        <div class="level-right">
          <transition name="slide">
            <Nav
              v-if="!isResponsive"
              :itemsNav="dataNamePages"
              @returnNavToBody="passIndexBodyToSkeleton"
            />
            <BurgerNav v-else @BurgerIsActive="ContainerIsActive"/>
          </transition>
        </div>
      </header>
      <transition name="slide">
        <ContainerNav
          v-if="containerIsActive"
          :itemsNav="dataNamePages"
          @returnNavMobileToBody="passIndexMobileBodyToSkeleton"
        />
      </transition>
      <Skeleton
        @returnSkeltonToBody="indexFromSlide"
        :indexToSkeleton="indexFromNav"
        :dataToSkeleton="dataNamePages"
        v-if="$route.name!=='notfound'"
      />
      <NotFound v-else/>
      <Footer style="height:1200px"/>
    </div>
    <div v-else id="main-body" class="container is-fluid is-marginless">
      <p>await ...</p>
    </div>
  </div>
</template>
<script>
import Skeleton from "./Templates/Skeleton.vue";
import NotFound from "./Templates/NotFound.vue";
import Nav from "@/components/Navs/Nav.vue";
import BurgerNav from "@/components/Navs/ResponsivesNavs/BurgerNav.vue";
import ContainerNav from "@/components/Navs/ResponsivesNavs/ContainerNav.vue";
import Footer from "@/components/Footers/Footer.vue";
import getApi from "@/services/api.js";
export default {
  name: "BodyApp",
  components: {
    Skeleton,
    NotFound,
    Footer,
    BurgerNav,
    ContainerNav,
    Nav
  },
  data() {
    return {
      dataNamePages: [],
      indexFromNav: null,
      isResponsive: Boolean,
      containerIsActive: false
    };
  },
  beforeMount() {
    this.fetchNamePage();
  },
  mounted() {
    this.TargetResponsive(window.innerWidth);
    this.EventResize();
  },
  watch: {
    indexFromNav(index) {
      console.log(index)
      this.indexFromNav = index;
    }
  },
  watch: {
    containerIsActive(bool) {
      if (bool) document.documentElement.style.overflow = "hidden";
      else document.documentElement.style = "";
    }
  },
  methods: {
    EventResize() {
      window.onresize = () => {
        this.TargetResponsive(window.innerWidth);
      };
    },
    TargetResponsive(width) {
      if (width <= 1023) this.isResponsive = true;
      else {
        this.isResponsive = false;
        this.containerIsActive = false;
      }
    },
    ContainerIsActive(ContainerIsActive) {
      this.containerIsActive = ContainerIsActive;
    },
    fetchNamePage() {
      getApi.getAllPage().then(res => (this.dataNamePages = res.data));
    },

    passIndexBodyToSkeleton(navIndex) {
      this.indexFromNav = navIndex;
    },
    passIndexMobileBodyToSkeleton(navIndex) {
      this.indexFromNav = navIndex;
    },
    indexFromSlide(slideIndex) {
      console.log(slideIndex)
      this.indexFromNav = slideIndex;
    }
  }
};
</script>

<style lang="scss">
.slide-leave-active {
  -webkit-animation-name: slideOutRight;
  animation-name: slideOutRight;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@-webkit-keyframes slideOutRight {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
  100% {
    visibility: hidden;
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }
}
@keyframes slideOutRight {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
  100% {
    visibility: hidden;
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }
}

.slide-enter-active {
  -webkit-animation-name: slideInRight;
  animation-name: slideInRight;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@-webkit-keyframes slideInRight {
  0% {
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
    visibility: visible;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
}
@keyframes slideInRight {
  0% {
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
    visibility: visible;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
}
.overflow-hidden {
  overflow: hidden;
}
</style>

