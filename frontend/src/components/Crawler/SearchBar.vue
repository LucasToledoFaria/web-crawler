<template>
  <div class="search-bar">
    <input v-model="url" type="text" placeholder="Enter URL" />
    <button @click="crawl">
      <span>Crawl</span>
    </button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      url: "",
    };
  },
  methods: {
    async crawl() {
      try {
        const response = await fetch("http://localhost:8080/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: this.url,
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
</style>
