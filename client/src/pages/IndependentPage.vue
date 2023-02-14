<template>
  <div class="container-fluid home position-fixed"></div>
  <div class="container-fluid" style="padding-top: 50px">
    <div class="container text-center">
      <div class="row g-1">
        <div class="col-3">
          <div class="row">
            <div class="container block_background">
              <announcement v-if="articleType === 'blog'"></announcement>
              <blog v-if="articleType === 'announcement'"></blog>
              <clock-master></clock-master>
              <earth></earth>
              <divination></divination>
            </div>
          </div>
        </div>
        <div class="col-9">
          <div class="row">
            <div class="offset-1 col-10 block_background">
              <div class="container">
                <table class="table" v-if="articleType === 'blog'">
                  <thead>
                    <tr><th scope="col">&#127774;博客</th></tr>
                  </thead>
                  <tbody id="index_blog_list" ref="index_blog_list">
                    <tr v-if="blog === null">
                      <td v-if="userStatus != null && userStatus.authority === 3">
                        服务器内部错误，请检查：<br>
                        1. 是否开启Flask服务器 <br>
                        2. 如已开启，请检查'/static/blog'中文件是否与数据库中文件匹配 <br>
                      </td>
                      <td v-else>
                        服务器内部错误，请联系管理员
                      </td>
                    </tr>
                    <tr v-else-if="blog === 'critical'">
                      <td>未找到相关博客</td>
                    </tr>
                    <tr v-else>
                      <td style="padding: 30px 0">
                        <p class="fs-1 fw-bold">{{ blog.blog_title }}</p>
                        <div class="blog text-start" :style="`word-wrap: break-word`">
                          <div v-html="blog.content"></div>
                        </div>
                        <br>
                        <p class="fs-6 fw-light text-secondary text-end">
                          <!--<span v-if="userStatus != null && userStatus.authority === 3">&nbsp;<u class="link-text" @click="deleteBlog(blog.blog_filename)">删除</u>&nbsp;|&nbsp;</span>-->
                          发布于 {{ blog.create_time }}
                        </p>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <table class="table" v-else-if="articleType === 'announcement'">
                  <thead>
                    <tr><th scope="col">&#128226;公告</th></tr>
                  </thead>
                  <tbody>
                    <tr v-if="announcement === null">
                      <td v-if="userStatus != null && userStatus.authority === 3">
                        服务器内部错误，请检查：<br>
                        1. 是否开启Flask服务器 <br>
                        2. 如已开启，请检查'/static/blog'中文件是否与数据库中文件匹配 <br>
                      </td>
                      <td v-else>
                        服务器内部错误，请联系管理员
                      </td>
                    </tr>
                    <tr v-else-if="announcement === 'critical'">
                      <td>未找到相关公告</td>
                    </tr>
                    <tr v-else>
                      <td style="padding: 30px 0">
                        <p class="fs-1 fw-bold">{{ announcement.announcement_title }}</p>
                        <div class="blog text-start" :style="`word-wrap: break-word`">
                          <div>{{ announcement.content }}</div>
                        </div>
                        <br>
                        <p class="fs-6 fw-light text-secondary text-end">
                          <!--<span v-if="userStatus != null && userStatus.authority === 3">&nbsp;<u class="link-text" @click="deleteBlog(blog.blog_filename)">删除</u>&nbsp;|&nbsp;</span>-->
                          发布于 {{ announcement.create_time }}
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
    </div>
  </div>
</template>

<script>
import Announcement from "@/components/Announcement";
import Blog from "@/components/Blog";
import ClockMaster from "@/components/ClockMaster";
import Divination from "@/components/Divination";
import Earth from "@/components/Earth";
import axios from "axios";
import {marked} from "marked";
import jwtDecode from "jwt-decode";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "IndependentPage",
  components: { Announcement, Blog, ClockMaster, Divination, Earth },
  data() {
    return {
      userStatus: null,
      articleType: null,
      articleId: 0,
      blog: null,
      announcement: null,
    }
  },
  methods: {
    displayArticle() {
      if (this.articleType === 'blog') {
        const path = `${this.httpUrl}/get_blog/${this.articleId}`
        axios.get(path)
          .then((res) => {
            if(res.data.error === null) {
              this.blog = res.data.blog
              this.blog.content = marked.parse(this.blog.content)
            }
            else
              this.blog = res.data.error
          })
          .catch((error) => {
            console.error(error)
          })
      }
      else if (this.articleType === 'announcement') {
        const path = `${this.httpUrl}/get_announcement/${this.articleId}`
        axios.get(path)
          .then((res) => {
            if(res.data.error === null)
              this.announcement = res.data.announcement
            else
              this.announcement = res.data.error
          })
          .catch((error) => {
            console.error(error)
          })
      }
    }
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
    this.articleType = this.$route.path.split('/')[1];
    this.articleId = this.$route.params.id;
    this.displayArticle();
  },
  updated() {
    if (this.articleType === this.$route.path.split('/')[1] && this.articleId === this.$route.params.id)
      return;

    this.articleType = this.$route.path.split('/')[1];
    this.articleId = this.$route.params.id;
    this.displayArticle();
  },
}
</script>

<style scoped>
.home {
  padding-top: 50px;
  width: 100%;
  height: 100%;
  background-image: url("@/assets/imgs/index-background.jpg");
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
.blog:deep(img) {
  width: 100%;
}
</style>