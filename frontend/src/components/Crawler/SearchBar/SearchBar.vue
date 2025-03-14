<template>
  <div>
    <div class="search-bar">
      <input v-model="url" type="text" placeholder="Enter URL" @keyup.enter="crawl" />
      <button @click="crawl" :disabled="loading">
        <span v-if="loading" class="spinner"></span>
        <span v-else>Crawl</span>
      </button>
      <button
        @click="toggleParams"
        class="gear-button"
        title="Optional Parameters"
      >
        <span :class="{ 'gear-icon': true, open: showParams }">⚙️</span>
      </button>
    </div>
    <div v-if="showParams" class="optional-params-wrapper">
      <OptionalParams v-model="params" />
    </div>
    <div>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    </div>
  </div>
</template>

<script>
import OptionalParams from "./OptionalParams.vue";

export default {
  name: "SearchBar",
  components: {
    OptionalParams,
  },
  data() {
    return {
      url: "",
      loading: false,
      errorMessage: "",
      successMessage: "",
      showParams: false,
      params: {
        max_depth: 3,
        max_urls: 200,
        max_connections: 20,
        max_host_connections: 10,
      },
    };
  },
  methods: {
    toggleParams() {
      this.showParams = !this.showParams;
    },
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
    validateParams(params) {
      const validatedParams = {};
      for (const key in params) {
        if (params[key] !== "") {
          if (params[key] < 1) {
            this.errorMessage = `${key.replace("_", " ")} must be 1 or more.`;
            return null;
          }
          validatedParams[key] = params[key];
        }
      }
      return validatedParams;
    },
    calculateMaxDepth(urlsDict, depth = 0) {
      if (!urlsDict.founded_links || urlsDict.founded_links.length === 0) {
        return depth;
      }
      return Math.max(
        ...urlsDict.founded_links.map((link) =>
          this.calculateMaxDepth(link, depth + 1)
        )
      );
    },
    async crawl() {
      this.loading = true;
      this.errorMessage = "";
      this.successMessage = "";
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
      const validatedParams = this.validateParams(this.params);
      if (!validatedParams) {
        this.loading = false;
        this.$emit("loading", false);
        return;
      }
      try {
        const response = await fetch(process.env.VUE_APP_API_URL, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: validatedUrl,
            ...validatedParams,
          }),
        });
        if (!response.ok) {
          throw new Error(await response.text());
        }
        const data = await response.json();
        this.$emit("crawl-success", data);
        const maxDepth = this.calculateMaxDepth(data.urls_dict);
        this.successMessage = `Crawl completed successfully. Found ${data.all_urls.length} URLs with a maximum depth of ${maxDepth}.`;
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

.gear-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  align-self: center;
  border-radius: 50%;
  padding: 0.3rem 0.3rem;
  margin-left: 0.5rem;
}

.gear-button:hover:enabled {
  background-color: #0057b315;
}

.gear-icon {
  transition: transform 0.3s;
}

.gear-icon.open {
  transform: rotate(90deg);
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

.success-message {
  color: green;
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
