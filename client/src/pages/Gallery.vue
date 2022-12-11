<template>
  <div class="container-fluid home position-fixed" style="background-color: black"></div>
  <div class="container-fluid" style="padding-top: 50px">
    <div class="row">
      <div class="container" id="gallery" ref="gallery" :style="{ width: `${galleryWidth}px` }">
        <div class="row">
          <div class="col-3 px-md-0 gallery-wall" :style="{ height: `${colHeight}px` }">
          </div>
          <div class="col-3 px-md-0 gallery-wall">
          </div>
          <div class="col-3 px-md-0 gallery-wall">
          </div>
          <div class="col-3 px-md-0 gallery-wall">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Gallery",
  data() {
    return {
      galleryWidth: null,
      galleryHeight: null,
      colWidth: null,
      colHeight: null,
    }
  },
  mounted() {
    let allCols = document.querySelectorAll(".gallery-wall");
    this.colWidth = allCols[0].clientWidth;
    this.colHeight = this.colWidth / 254 * 591; // “gallery_wall.png”的宽高比
    let windowWidth = window.innerWidth, windowHeight = window.innerHeight - 50;
    if (this.colHeight <= windowHeight)
      this.galleryWidth = windowWidth;
    else {
      this.galleryWidth = windowWidth / this.colHeight * windowHeight;
      this.colHeight = windowHeight;
    }
  }
}
</script>

<style scoped>
.home {
  padding-top: 50px;
  width: 100%;
  height: 100%;
  /* background-image: url("@/assets/imgs/index-background.jpg"); */
  background-size: cover;
  position: fixed;
  z-index: -1;
}
.gallery-wall {
  background-image: url("@/assets/imgs/gallery_wall.png");
  background-size: contain;
}
</style>