<template>
  <div class="container-fluid home"></div>
  <div>Space</div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Space"
}
</script>

<style scoped>
.home {
  padding-top: 50px;
  width: 100%;
  height: 100%;
  background-image: url("@/assets/imgs/index-background.png");
  background-size: cover;
  position: absolute;
}
</style>