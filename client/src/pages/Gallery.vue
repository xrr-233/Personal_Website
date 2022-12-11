<template>
  <div class="container-fluid home position-fixed" style="background-color: black"></div>
  <div class="container-fluid" style="padding-top: 50px">
    <div class="row">
      <div class="container" id="gallery" ref="gallery" :style="{ width: `${galleryWidth}px` }">
        <div class="row">
          <div v-for="i in 4" :key="i" class="col-3 px-md-0 gallery-wall" :style="{ height: `${colHeight}px` }">
            <div v-if="(i - 1) * 2 < collectionsList.length" class="gallery-block-empty"></div>
            <div v-if="(i - 1) * 2 < collectionsList.length" class="gallery-block">
              <collection :id="collectionsList[(i - 1) * 2].id" :title="collectionsList[(i - 1) * 2].proj_title" :link="collectionsList[(i - 1) * 2].proj_link"></collection>
            </div>
            <div v-if="(i - 1) * 2 + 1 < collectionsList.length" class="gallery-block">
              <collection :id="collectionsList[i * 2 - 1].id" :title="collectionsList[i * 2 - 1].proj_title" :link="collectionsList[i * 2 - 1].proj_link"></collection>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Collection from "@/components/Collection";
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Gallery",
  inject: ["httpUrl"],
  components: {
    Collection
  },
  data() {
    return {
      galleryWidth: null,
      galleryHeight: null,
      colWidth: null,
      colHeight: null,
      collectionsList: [],
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

    const this_ = this;
    addEventListener("resize", (e) => {
      // console.log(e.target.innerWidth, e.target.innerHeight);
      this_.colWidth = allCols[0].clientWidth;
      this_.colHeight = this_.colWidth / 254 * 591; // “gallery_wall.png”的宽高比
      let windowWidth = e.target.innerWidth, windowHeight = e.target.innerHeight - 50;
      if (this_.colHeight <= windowHeight) {
        this_.galleryWidth = windowHeight / 591 * 254 * 4;
        this_.colHeight = windowHeight;
      }
      else {
        this_.galleryWidth = windowWidth / this_.colHeight * windowHeight;
        this_.colHeight = windowHeight;
      }
    });

    const path = `${this.httpUrl}/get_collections`
    axios.post(path)
        .then((res) => {
          if(res.data.error === null)
            this.collectionsList = res.data.collections;
        })
        .catch((error) => {
          console.error(error)
        })
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
.gallery-block-empty {
  height: 10%;
  width: 100%;
}
.gallery-block {
  height: 35%;
  width: 100%;
}
</style>