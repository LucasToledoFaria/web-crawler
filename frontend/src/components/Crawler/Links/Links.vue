<script setup>
import { defineProps } from 'vue';
import TreeItem from "./TreeItem.vue";

const props = defineProps({
  treeData: Object
});
</script>

<template>
  <div>
    <TreeItem :model="treeData" />
  </div>
</template>


