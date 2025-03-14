<template>
  <div class="download-buttons">
    <button @click="downloadJson" :disabled="!responseData">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        fill="currentColor"
        class="bi bi-file-earmark-arrow-down"
        viewBox="0 0 16 16"
      >
        <path
          d="M8 5a.5.5 0 0 1 .5.5v5.793l1.146-1.147a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 1 1 .708-.708L7.5 11.293V5.5A.5.5 0 0 1 8 5z"
        />
        <path
          d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3-.5a.5.5 0 0 1-.5-.5V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V5h-2.5z"
        />
      </svg>
      URLs data (.json)
    </button>
    <button @click="downloadTxt" :disabled="!responseData">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        fill="currentColor"
        class="bi bi-file-earmark-arrow-down"
        viewBox="0 0 16 16"
      >
        <path
          d="M8 5a.5.5 0 0 1 .5.5v5.793l1.146-1.147a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 1 1 .708-.708L7.5 11.293V5.5A.5.5 0 0 1 8 5z"
        />
        <path
          d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3-.5a.5.5 0 0 1-.5-.5V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V5h-2.5z"
        />
      </svg>
      All URLs (.txt)
    </button>
  </div>
</template>

<script>
export default {
  name: "DownloadButtons",
  props: {
    responseData: {
      type: Object,
      required: true,
    },
  },
  methods: {
    downloadJson() {
      const dataStr =
        "data:text/json;charset=utf-8," +
        encodeURIComponent(
          JSON.stringify(this.responseData.urls_dict, null, 2)
        );
      const downloadAnchorNode = document.createElement("a");
      downloadAnchorNode.setAttribute("href", dataStr);
      downloadAnchorNode.setAttribute("download", "crawl_result.json");
      document.body.appendChild(downloadAnchorNode);
      downloadAnchorNode.click();
      downloadAnchorNode.remove();
    },
    downloadTxt() {
      const dataStr =
        "data:text/plain;charset=utf-8," +
        encodeURIComponent(this.responseData.all_urls.join("\n"));
      const downloadAnchorNode = document.createElement("a");
      downloadAnchorNode.setAttribute("href", dataStr);
      downloadAnchorNode.setAttribute("download", "all_urls.txt");
      document.body.appendChild(downloadAnchorNode);
      downloadAnchorNode.click();
      downloadAnchorNode.remove();
    },
  },
};
</script>

<style scoped>
.download-buttons {
  display: flex;
  gap: 1rem;
  margin: 1rem 0;
  flex-direction: row;
}

button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: #0056b3;
}
</style>
