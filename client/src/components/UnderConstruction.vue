<template>
  <div class="container-fluid home">
    <div class="container block_background">敬请期待</div>
  </div>
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
  position: absolute;
}
.block_background {
  background: rgba(255, 255, 255, 0.8);
}
</style>