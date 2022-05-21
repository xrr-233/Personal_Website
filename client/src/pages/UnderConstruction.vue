<template>
  <div class="container-fluid home"></div>
  <div class="container block_background" style="padding-top: 50px">敬请期待</div>
</template>

<script>
export default {
  name: "UnderConstruction"
}
</script>

<style scoped>
.home {
  padding-top: 50px;
  width: 100%;
  height: 100%;
  background-image: url("../../public/index-background.jpg");
  background-size: cover;
  position: fixed;
  z-index: -1;
}
.block_background {
  background: rgba(255, 255, 255, 0.8);
}
</style>