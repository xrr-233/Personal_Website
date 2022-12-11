<template>
  <div class="container" style="height: 100%">
    <div class="row" style="height: 75%">
      <div class="container text-center position-relative" style="height: 100%">
        <img class="position-absolute top-50 start-50 translate-middle" src="@/assets/imgs/gallery_waiting.jpg" alt="" style="height: 75%" ref="my-hover-img-int" draggable="false">
        <img class="position-absolute top-50 start-50 translate-middle" src="@/assets/imgs/gallery_frame.png" alt="" style="height: 100%" ref="my-hover-img-ext" draggable="false">
      </div>
    </div>
    <div class="row" style="height: 25%">
      <p class="text-center collection-title" ref="my-hover-text">{{ this.title }}</p>
    </div>
  </div>
</template>

<script>
import "@/assets/css/font.css"
import axios from "axios";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Collection",
  props: ['id', 'title', 'link'],
  methods: {
    myHoverIn() {
      this.$refs['my-hover-img-int'].style.boxShadow = "0 0 20px 10px rgba(255, 255, 64, 0.5)";
      this.$refs['my-hover-text'].style.fontWeight = "bold";
      this.$refs['my-hover-text'].style.textDecoration = "underline";
    },
    myHoverOut() {
      this.$refs['my-hover-img-int'].style.boxShadow = null;
      this.$refs['my-hover-text'].style.fontWeight = "normal";
      this.$refs['my-hover-text'].style.textDecoration = null;
    },
  },
  mounted() {
    if (this.link != null) {
      this.$refs['my-hover-img-ext'].onmouseenter = () => { this.myHoverIn(); }
      this.$refs['my-hover-text'].onmouseenter = () => { this.myHoverIn(); }
      this.$refs['my-hover-img-ext'].onmouseleave = () => { this.myHoverOut(); }
      this.$refs['my-hover-text'].onmouseleave = () => { this.myHoverOut(); }
      this.$refs['my-hover-img-ext'].onmouseup = () => { window.open(this.link); }
      this.$refs['my-hover-text'].onmouseup = () => { window.open(this.link); }
      this.$refs['my-hover-img-ext'].style.cursor = "pointer";
      this.$refs['my-hover-text'].style.cursor = "pointer";
    }
    else {
      this.$refs['my-hover-img-ext'].title = "This project is still not public"
      this.$refs['my-hover-text'].title = "This project is still not public"
    }

    const path = `${this.httpUrl}/get_collection_img`, this_ = this;
    axios.post(path, {
        'id': this.id,
      })
        .then((res) => {
          if(res.data.error === null) {
            // console.log(res);
            this_.$refs['my-hover-img-int'].src = `data:image/png;base64,${res.data.base64}`
          }
        })
        .catch((error) => {
          console.error(error);
        })
  }
}
</script>

<style scoped>
.collection-title {
  font-family: "victoria", serif;
  font-size: 20px;
}
</style>