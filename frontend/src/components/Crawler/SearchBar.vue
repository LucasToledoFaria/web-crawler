<template>
  <div>
    <div class="search-bar">
      <input v-model="url" type="text" placeholder="Enter URL" />
      <button @click="crawl" :disabled="loading">
        <span v-if="loading" class="spinner"></span>
        <span v-else>Crawl</span>
      </button>
    </div>
    <div>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      url: "",
      loading: false,
      errorMessage: "",
    };
  },
  methods: {
    validateUrl(url) {
      try {
        const parsedUrl = new URL(url);
        return parsedUrl.href;
      } catch (_) {
        if (!/^https?:\/\//i.test(url)) {
          const prefixedUrl = `https://${url}`;
          try {
            const parsedUrl = new URL(prefixedUrl);
            if (parsedUrl.hostname.includes(".")) {
              return parsedUrl.href;
            } else {
              throw new Error("Invalid URL");
            }
          } catch (_) {
            throw new Error("Invalid URL");
          }
        }
        throw new Error("Invalid URL");
      }
    },
    async crawl() {
      this.loading = true;
      this.errorMessage = "";
      this.$emit("loading", true);
      let validatedUrl;
      try {
        validatedUrl = this.validateUrl(this.url);
      } catch (error) {
        this.errorMessage = "Invalid URL. Please enter a valid URL.";
        this.loading = false;
        this.$emit("loading", false);
        return;
      }
      try {
        const response = await fetch("http://localhost:8080/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: validatedUrl,
            max_depth: 3,
            max_urls: 200,
            max_connections: 20,
            max_host_connections: 10,
          }),
        });
        if (!response.ok) {
          throw new Error(await response.text());
        }
        const data = await response.json();
        this.$emit("crawl-success", data);
        console.log(data);
      } catch (error) {
        console.error("Error:", error);
        this.errorMessage =
          "An error occurred while crawling the URL. Please ensure the URL is valid and try again.";
      } finally {
        this.loading = false;
        this.$emit("loading", false);
      }
    },
  },
};
</script>

<style scoped>
.search-bar {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin: 1rem;
}

input {
  padding: 0.5rem;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 4px 0 0 4px;
  outline: none;
}

button {
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-left: none;
  border-radius: 0 4px 4px 0;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: #0056b3;
}

.spinner {
  border: 2px solid #f3f3f3;
  border-top: 2px solid #007bff;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  animation: spin 1s linear infinite;
}

.error-message {
  color: red;
  margin-bottom: 1.5rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
