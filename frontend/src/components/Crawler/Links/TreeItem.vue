<script setup>
import { ref, computed, nextTick } from "vue";

const props = defineProps({
  model: {
    type: Object,
    required: true,
  },
  maxWidth: {
    type: String,
    default: '90vw'
  }
});

const isOpen = ref({});
const isFolder = computed(() => {
  return (
    props.model &&
    props.model.founded_links &&
    props.model.founded_links.length > 0
  );
});

const folderCount = computed(() => {
  return isFolder.value ? props.model.founded_links.length : 0;
});

function toggle(link) {
  isOpen.value[link] = !isOpen.value[link];
}

function openLink(url) {
  if (typeof window !== "undefined") {
    window.open(url, "_blank");
  }
}

function scrollToParent(link, event) {
  if (event.target.classList.contains("nested-links")) {
    nextTick(() => {
      const parentElement = document.getElementById(link);
      if (parentElement) {
        const headerOffset = 80;
        const elementPosition = parentElement.getBoundingClientRect().top;
        const offsetPosition =
          elementPosition + window.scrollY - headerOffset;
        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth",
        });
      }
    });
  }
}
</script>

<template>
  <div class="link-container" v-if="model">
    <div :id="model.link" class="link-box" @click="toggle(model.link)" :style="{ maxWidth: maxWidth }">
      <span class="icon">
        {{ isFolder ? (isOpen[model.link] ? "▾" : "▸") : "─" }}
      </span>
      <span class="link-text">
        <strong>{{ model.link }}</strong>
      </span>
      <span v-if="isFolder" class="count">({{ folderCount }})</span>
      <button class="open-link" @click.stop="openLink(model.link)">
        <svg
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path
            d="M18 13V19A2 2 0 0 1 16 21H5A2 2 0 0 1 3 19V8A2 2 0 1 5 6H11"
          />
          <polyline points="15 3 21 3 21 9" />
          <line x1="10" y1="14" x2="21" y2="3" />
        </svg>
      </button>
    </div>
    <transition name="fade">
      <div
        v-show="isOpen[model.link]"
        v-if="isFolder"
        class="nested-links"
        @click.stop="(event) => scrollToParent(model.link, event)"
      >
        <TreeItem
          v-for="child in model.founded_links"
          :key="child.link"
          :model="child"
          :maxWidth="maxWidth"
        />
      </div>
    </transition>
  </div>
</template>

<style scoped>
.link-container {
  margin: 4px 0;
}

.link-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  background-color: #f9f9f9;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
  word-wrap: break-word;
}

.link-box:hover {
  background-color: #e3e3e3;
}

.icon {
  margin-right: 8px;
  font-size: 14px;
  color: #555;
}

.link-text {
  flex: 1;
  font-size: 14px;
  color: #333;
  white-space: normal;
  overflow: hidden;
  text-overflow: ellipsis;
}

.count {
  margin-left: 8px;
  font-size: 12px;
  color: #666;
}

.open-link {
  padding: 4px;
  border: none;
  background: none;
  cursor: pointer;
  color: #007bff;
  transition: color 0.3s;
  display: flex;
  align-items: center;
}

.open-link svg {
  width: 18px;
  height: 18px;
}

.open-link:hover {
  color: #0056b3;
}

.nested-links {
  margin-left: 16px;
  padding-left: 8px;
  border-left: 2px solid #ccc;
  cursor: pointer;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease-in-out;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
