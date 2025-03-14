<template>
  <div class="optional-params">
    <div class="param-row">
      <label :title="descriptions.max_urls">
        Max URLs:
        <input v-model.number="params.max_urls" type="number" min="1" />
      </label>
      <label :title="descriptions.max_connections">
        Max Connections:
        <input v-model.number="params.max_connections" type="number" min="1" />
      </label>
    </div>
    <div class="param-row">
      <label :title="descriptions.max_depth">
        Max Depth:
        <input v-model.number="params.max_depth" type="number" min="1" />
      </label>
      <label :title="descriptions.max_host_connections">
        Max Host Connections:
        <input
          v-model.number="params.max_host_connections"
          type="number"
          min="1"
        />
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: "OptionalParams",
  props: {
    modelValue: {
      type: Object,
      required: true,
    },
  },
  computed: {
    params: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit("update:modelValue", value);
      },
    },
  },
  data() {
    return {
      descriptions: {
        max_depth: "The maximum depth to crawl (default: 3).",
        max_urls: "The maximum number of URLs to crawl (default: 200).",
        max_connections:
          "The maximum number of concurrent connections (default: 20).",
        max_host_connections:
          "The maximum number of concurrent connections per host (default: 10).",
      },
    };
  },
};
</script>

<style scoped>
.optional-params {
  display: flex;
  flex-direction: column;
  margin: 1rem 0;
  font-family: Arial, sans-serif;
  color: #011d39;
  font-size: 0.9rem;
}

.param-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

label {
  margin-bottom: 0.5rem;
  margin-right: 0.5rem;
  margin-left: 0.5rem;
}

input {
  margin-left: 0.5rem;
  padding: 0.25rem;
  width: 50px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
  font-family: Arial, sans-serif;
  color: #011d39;
}
</style>
