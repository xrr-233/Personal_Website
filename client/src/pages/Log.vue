<template>
  <div class="container-fluid home position-fixed"></div>
  <div class="container" style="padding-top: 50px">
    <div class="row">
      <div class="offset-3 col-6 block_background">
        <div class="container-fluid" v-html="logContent" style="padding-top: 50px; padding-bottom: 50px"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from "marked";
import axios from "axios";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Log",
  data() {
    return {
      logContent: ""
    }
  },
  mounted() {
    const path = `${this.httpUrl}/get_log`;
    axios.get(path)
      .then((res) => {
        if(res.data.error === null)
          this.logContent = marked.parse(res.data.content);
        else
          this.logContent = "日志文件不存在！";
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
  background-image: url("@/assets/imgs/index-background.png");
  background-size: cover;
  position: fixed;
  z-index: -1;
}
.block_background {
  background: rgba(255, 255, 255, 0.8);
}
</style>