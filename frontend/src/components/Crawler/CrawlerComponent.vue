<template>
  <div>
    <SearchBar @crawl-success="handleCrawlSuccess" @loading="setLoading" />
    <DownloadButtons v-if="responseData" :responseData="responseData" />
    <div v-if="loading" class="spinner"></div>
    <Links v-if="responseData" :treeData="responseData.urls_dict" />
  </div>
</template>

<script>
import SearchBar from "./SearchBar/SearchBar.vue";
import Links from "./Links/Links.vue";
import DownloadButtons from "./DownloadButtons.vue";

export default {
  name: "CrawlerComponent",
  components: {
    SearchBar,
    Links,
    DownloadButtons,
  },
  data() {
    return {
      responseData: null,
      loading: false,
    };
  },
  methods: {
    handleCrawlSuccess(data) {
      this.responseData = data;
      this.loading = false;
    },
    setLoading(isLoading) {
      this.loading = isLoading;
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

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
