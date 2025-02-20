<template>
  <header>
    <h1>Web Crawler</h1>
  </header>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
header {
  background-color: #007bff;
  padding: 0.8rem;
  text-align: center;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 1000;
}

h1 {
  margin: 0;
  font-size: 2rem;
  font-weight: bold;
}
</style>
