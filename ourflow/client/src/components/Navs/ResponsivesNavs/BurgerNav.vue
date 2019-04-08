<template>
  <div
    @click="ClickOnBurger"
    id="menu-burger-click"
    :class="{ 'menu-active': IsActive, 'menu-burger-container': true }"
  >
    <div class="menu-burger-frite-boisson"></div>
  </div>
</template>
<script>
export default {
  name: "BurgerNav",
  data() {
    return {
      IsActive: false
    };
  },
  computed: {
    indexChange() {
      return this.$store.getters.getIndex;
    }
  },
  watch: {
    indexChange() {
      this.IsActive = false;
    }
  },
  methods: {
    ClickOnBurger() {
      this.ClassIsActive();
      this.PassEventToBody();
    },
    ClassIsActive() {
      if (this.IsActive) this.IsActive = false;
      else this.IsActive = true;
    },
    PassEventToBody() {
      this.$emit("BurgerIsActive", this.IsActive);
    }
  }
};
</script>

<style lang="scss">
.menu-burger-container {
  width: 50px;
  height: 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  position: fixed;
  top: 10px;
  right: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: rotate(-360deg);
  transition-duration: 0.2s;
  background: #fff;
}

.menu-burger-frite-boisson {
  width: 30px;
  height: 4px;
  background: #21201f;
  border-radius: 2px;
  position: relative;
}

.menu-burger-frite-boisson::before {
  content: "";
  position: absolute;
  width: 30px;
  height: 4px;
  left: 0;
  transform: translateY(-8px);
  background-color: #21201f;
  border-radius: 2px;
  transition-duration: 0.2s;
}

.menu-burger-frite-boisson::after {
  content: "";
  position: absolute;
  width: 30px;
  height: 4px;
  left: 0;
  transform: translateY(8px);
  background-color: #21201f;
  border-radius: 2px;
  transition-duration: 0.2s;
}

.menu-active .menu-burger-frite-boisson::before {
  transform: rotate(45deg);
}

.menu-active .menu-burger-frite-boisson::after {
  transform: rotate(-45deg);
}

.menu-active {
  transform: rotate(360deg);
  transition-duration: 0.3s;
}

.menu-active .menu-burger-frite-boisson {
  background: #fff;
  transition-duration: 0.3s;
}
</style>
