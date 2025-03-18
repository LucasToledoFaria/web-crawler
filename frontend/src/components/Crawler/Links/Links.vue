<script setup>
import { defineProps, computed } from 'vue';
import TreeItem from "./TreeItem.vue";
import { calculateMaxDepth } from "@/utils/calculateMaxDepth";

const props = defineProps({
  treeData: Object
});

const maxWidth = computed(() => {
  const depth = calculateMaxDepth(props.treeData);
  return `${95 - depth * 8}vw`;
});
</script>

<template>
  <div>
    <TreeItem :model="treeData" :maxWidth="maxWidth" />
  </div>
</template>


