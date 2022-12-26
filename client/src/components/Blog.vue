<template>
  <div class="home_blog">
    <table class="table">
      <thead>
        <tr><th scope="col">&#127774;博客</th></tr>
      </thead>
      <tbody id="my_table" ref="my_table">
        <tr v-if="blogs_num === 0"><td><div class="text">主人目前还没有文章哦~</div></td></tr>
        <tr v-else v-for="blog in blogs" :key="blog.blog_title"><td><div class="text fw-bold"><u>{{ blog.blog_title }}</u></div></td></tr>
        <tr v-if="blogs_num > max_title_num"><td><div class="fw-bold">查看更多</div></td></tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Blog",
  data() {
    return {
      blogs_num: 0,
      blogs: [],
      max_title_num: 4,
    }
  },
  methods: {
    askForBlogTitles() {
      const path = `${this.httpUrl}/get_blog_titles`
      axios.post(path, {
        'max_title_num': this.max_title_num,
      })
        .then((res) => {
          if(res.data.error === null) {
            this.blogs_num = res.data.number;
            this.blogs = res.data.blogs;
          }
          else {
            this.blogs_num = null
          }
        })
        .catch((error) => {
          console.error(error)
          this.blogs_num = null
        })
    },
  },
  mounted() {
    this.askForBlogTitles();
  }
}
</script>

<style scoped>
.text {
  float: left;
  white-space: nowrap;
  overflow: hidden;
}
</style>