<template>
  <div class="container-fluid home">
    <div class="container text-center">
      <div class="row">
        <div class="col-3 block_background">
          <announcement></announcement>
          <clock-master></clock-master>
        </div>
        <div class="offset-6 col-3 block_background">
          <divination></divination>
        </div>
      </div>
    </div>
  </div>
  <div class="container text-center" style="padding-top: 50px">
    <div class="offset-3 col-6">
      <div class="row">
        <div class="offset-1 col-10 block_background">
          <div class="container">
            <table class="table">
              <thead>
                <tr><th scope="col">&#127774;博客</th></tr>
              </thead>
              <tbody id="index_blog_list" ref="index_blog_list">
                <tr v-if="blogs_num === null"><td>服务器内部错误</td></tr>
                <tr v-if="blogs_num === 0"><td>主人目前还没有文章哦~</td></tr>
                <tr v-for="b in blogs" :key="b.create_time">
                  <td style="padding: 30px 0">
                    <p class="fs-1 fw-bold">{{ b.blog_title }}</p>
                    <div class="blog text-start" :style="{ width: td_width + 'px', wordWrap: 'break-word' }">
                    <!--<div class="blog text-start" :style="`width: ${td_width}px; word-wrap: break-word`">-->
                      <div v-html="b.content"></div>
                    </div>
                    <br>
                    <p class="fs-6 fw-light text-secondary text-end">
                      <span v-if="userStatus != null && userStatus.authority === 3">&nbsp;<u class="link-text" @click="deleteBlog(b.blog_filename)">删除</u>&nbsp;|&nbsp;</span>
                      发布于 {{ b.create_time }}
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from 'marked'
import Announcement from "@/components/Announcement";
import ClockMaster from "@/components/ClockMaster";
import Divination from "@/components/Divination";
import axios from "axios";
import jwtDecode from "jwt-decode";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Index",
  components: { Divination, ClockMaster, Announcement },
  data() {
    return {
      userStatus: null,
      td_width: 0,
      blogs_num: 0,
      blogs: [],
    }
  },
  methods: {
    askForBlogs(start_page, per_page) {
      this.td_width = this.$refs.index_blog_list.offsetWidth

      const path = `${this.httpUrl}/ask_for_blogs`
      axios.post(path, {
        'start_page': start_page,
        'per_page': per_page
      })
        .then((res) => {
          if(res.data.error === null) {
            this.blogs_num = res.data.number
            this.blogs = res.data.blogs
            for(let i = 0; i < res.data.number; i++) {
              this.blogs[i].content = marked.parse(this.blogs[i].content)
            }
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
    deleteBlog(blog_filename) {
      const path = `${this.httpUrl}/delete_blog`
      axios.post(path, {
        'blog_filename': blog_filename,
      })
        .then((res) => {
          if(res.data.status === 'success')
            alert('删除成功')
          else
            alert('博客已删除')
          this.$router.push({ name: 'RefreshMedia' })
        })
        .catch((error) => {
          console.error(error)
        })
    },
  },
  created() {
    if(localStorage.getItem('token') !== null) {
      try {
        this.userStatus = jwtDecode(localStorage.getItem('token'))
        if(this.userStatus.nickname !== null)
          this.userName = this.userStatus.nickname
        else
          this.userName = this.userStatus.user_name
      }
      catch {
        localStorage.removeItem('token')
      }
    }
  },
  mounted() {
    this.askForBlogs(1, 10)
    //
    /*{% for i in range(blog_articles|length) %}
        $("#index_blog_list").append(tr);
        $.get('{{ url_for('static', filename='blog/' + blog_articles[i].blog_filename + '.md') }}', function(response, status, xhr){
            $(".blog").eq({{ i }}).html(marked.parse(response));
        });
        //$(".blog").html("<h1>{{ i }}</h1>");
    {% endfor %}*/
  }
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
.link-text:hover {
  cursor: pointer;
  color: blue;
}
</style>