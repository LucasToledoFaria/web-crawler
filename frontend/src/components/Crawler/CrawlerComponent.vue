<template>
  <div>
    <SearchBar @crawl-success="handleCrawlSuccess" />
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";

export default {
  name: "CrawlerComponent",
  components: {
    SearchBar,
  },
  data() {
    return {
      responseData: null,
    };
  },
  methods: {
    handleCrawlSuccess(data) {
      this.responseData = data;
    },
  },
};
</script>

<style scoped>
div {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
