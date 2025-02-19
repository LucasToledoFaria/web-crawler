<template>
  <div class="app-container">
    <Header />
  </div>
</template>

<script>
import Header from "./components/Structure/Header.vue";

export default {
  name: "App",
  components: {
    Header,
  },
  data() {
    return {
    };
  },
};
</script>

<style scoped>
.app-container {
  padding-top: 4rem;
  padding-left: 1rem;
  padding-right: 1rem;
}
</style>
