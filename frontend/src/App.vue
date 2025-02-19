<template>
  <div class="app-container">
    <Header />
    <CrawlerComponent />
  </div>
</template>

<script>
import Header from "./components/Structure/Header.vue";
import CrawlerComponent from "./components/Crawler/CrawlerComponent.vue";

export default {
  name: "App",
  components: {
    Header,
    CrawlerComponent,
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
