<template>
  <div>
    <SearchBar @crawl-success="handleCrawlSuccess" />
    <Links v-if="responseData" :treeData="responseData.urls_dict" />
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";
import Links from "./Links/Links.vue";

export default {
  name: "CrawlerComponent",
  components: {
    SearchBar,
    Links,
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
