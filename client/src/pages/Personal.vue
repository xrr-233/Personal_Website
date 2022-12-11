<template>
  <div class="container-fluid home position-fixed"></div>
  <div class="container text-start" style="padding-top: 50px">
    <div class="row g-1">
      <div class="col-3">
        <div class="row">
          <div class="container block_background" style="padding-top: 20px; padding-bottom: 20px">
            <div class="container rounded-3 tab">个人中心</div>
            <div class="container rounded-3 tab">安全</div>
            <div v-if="userStatus != null && userStatus.authority === 3" class="container rounded-3 tab">发布博客</div>
            <div v-if="userStatus != null && userStatus.authority === 3" class="container rounded-3 tab">发布公告</div>
          </div>
        </div>
      </div>
      <div class="col-9">
        <div class="row">
          <div class="offset-1 col-10 block_background">
            <div class="row tab-block">
              <div class="container">
                <div class="container">

                </div>
              </div>
            </div>
            <div class="row tab-block">
              <div class="container">
                <div class="container pt-5">
                  <h4>修改密码</h4>
                  <hr>
                  <div class="row mb-3">
                    <div class="col-auto">
                      <label for="old_password" class="col-form-label">旧密码</label>
                    </div>
                    <div class="col-auto">
                      <input type="password" id="old_password" ref="old_password" class="form-control" aria-describedby="old_password_feedback" required>
                      <div id="old_password_feedback" ref="old_password_feedback" class="invalid-feedback"></div>
                    </div>
                  </div>
                  <div class="row mb-3">
                    <div class="col-auto">
                      <label for="new_password" class="col-form-label">新密码</label>
                    </div>
                    <div class="col-auto">
                      <input type="password" id="new_password" ref="new_password" class="form-control" aria-describedby="new_password_feedback" required>
                      <div id="new_password_feedback" ref="new_password_feedback" class="invalid-feedback"></div>
                    </div>
                  </div>
                  <div class="row mb-3">
                    <div class="col-auto">
                      <label for="new_password2" class="col-form-label">再次输入新密码</label>
                    </div>
                    <div class="col-auto">
                      <input type="password" id="new_password2" ref="new_password2" class="form-control" aria-describedby="new_password2_feedback" required>
                      <div id="new_password2_feedback" ref="new_password2_feedback" class="invalid-feedback"></div>
                    </div>
                  </div>
                  <button type="submit" class="btn btn-outline-primary btn-sm" @click="changePassword">提交</button>
                </div>
                <div class="container pt-5">
                </div>
              </div>
            </div>
            <div class="row tab-block" v-if="userStatus != null && userStatus.authority === 3">
              <div class="container">
                <div class="container pt-5">
                  <h4>发布博客</h4>
                  <hr>
                  <form id="blog_form" @submit.prevent novalidate>
                    <div class="mb-3">
                      <label for="blog_title" class="form-label">博客标题</label>
                      <input class="form-control" type="text" id="blog_title" ref="blog_title" name="blog_title" aria-describedby="blog_title_feedback" required>
                      <div id="blog_title_feedback" ref="blog_title_feedback" class="invalid-feedback"></div>
                    </div>
                    <div class="mb-3">
                      <label for="form_file" class="form-label">请上传markdown(.md)文件</label>
                      <input class="form-control" type="file" id="form_file" ref="form_file" name="form_file" accept=".md" aria-describedby="form_file_feedback" required>
                      <div id="form_file_feedback" ref="form_file_feedback" class="invalid-feedback"></div>
                    </div>
                    <button class="btn btn-outline-primary btn-sm" @click="submitBlog()">提交</button>
                  </form>
                </div>
                <div class="container pt-5">
                </div>
              </div>
            </div>
            <div class="row tab-block" v-if="userStatus != null && userStatus.authority === 3">
              <div class="container">
                <div class="container pt-5">
                  <h4>发布公告</h4>
                  <hr>
                  <form id="announcement_form" @submit.prevent novalidate>
                    <div class="mb-3">
                      <label for="announcement_title" class="form-label">公告标题</label>
                      <input class="form-control" type="text" id="announcement_title" ref="announcement_title" name="announcement_title" aria-describedby="announcement_title_feedback" required>
                      <div id="announcement_title_feedback" ref="announcement_title_feedback" class="invalid-feedback"></div>
                    </div>
                    <div class="mb-3">
                      <label for="form_file" class="form-label">请输入公告内容</label>
                      <textarea class="form-control" id="form_content" ref="form_content" name="form_content" aria-describedby="form_content_feedback" required></textarea>
                      <div id="form_content_feedback" ref="form_content_feedback" class="invalid-feedback"></div>
                    </div>
                    <button class="btn btn-outline-primary btn-sm" @click="submitAnnouncement()">提交</button>
                  </form>
                </div>
                <div class="container pt-5">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jwtDecode from "jwt-decode"
import axios from "axios"

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Personal",
  data() {
    return {
      userStatus: null,
      screenWidth: 0,
      screenHeight: 0,
      scrollY: 0,
    }
  },
  methods: {
    changePassword() {
      const old_password = this.$refs.old_password, new_password = this.$refs.new_password, new_password2 = this.$refs.new_password2;
      const old_password_feedback = this.$refs.old_password_feedback, new_password_feedback = this.$refs.new_password_feedback, new_password2_feedback = this.$refs.new_password2_feedback;
      old_password.classList.remove('is-valid')
      new_password.classList.remove('is-valid')
      new_password2.classList.remove('is-valid')
      old_password.classList.remove('is-invalid')
      new_password.classList.remove('is-invalid')
      new_password2.classList.remove('is-invalid')
      let isErrorBeforePost = false
      if(old_password.value === "") {
        old_password_feedback.innerText = "输入不能为空"
        old_password.classList.add('is-invalid')
        isErrorBeforePost = true
      }
      if(new_password.value === "") {
        new_password_feedback.innerText = "输入不能为空"
        new_password.classList.add('is-invalid')
        isErrorBeforePost = true
      }
      if(new_password2.value === "") {
        new_password2_feedback.innerText = "输入不能为空"
        new_password2.classList.add('is-invalid')
        isErrorBeforePost = true
      }
      if(!isErrorBeforePost && new_password.value !== new_password2.value) {
        new_password_feedback.innerText = "两次输入的密码不一致"
        new_password2_feedback.innerText = "两次输入的密码不一致"
        new_password.classList.add('is-invalid')
        new_password2.classList.add('is-invalid')
      }
      if(!isErrorBeforePost) {
        const path = `${this.httpUrl}/change_password`
        axios.post(path, {
          'email': this.userStatus.email,
          'old_password': old_password.value,
          'new_password': new_password.value,
        })
          .then((res) => {
            if(res.data.status === "success") {
              old_password.value = ""
              new_password.value = ""
              new_password2.value = ""
              old_password.classList.add('is-valid')
              new_password.classList.add('is-valid')
              new_password2.classList.add('is-valid')
            }
            else {
              if(res.data.msg === "user_not_exist") {
                localStorage.removeItem('token')
                alert("你这个用户不乖哦~居然私自篡改token！不过我全部防出去，防出去了嗷（马保国并感")
                this.$router.push({ name: 'Index' })
                // 一般是不会出现这个情况啦，不过为了代码好看点留着
                // 目前导到Index不会清空全局userStatus变量，哪天来填坑吧
              }
              else if(res.data.msg === "wrong_password") {
                old_password_feedback.innerText = "密码错误"
                old_password.classList.add('is-invalid')
              }
            }
          })
          .catch((error) => {
            console.error(error)
          })
      }
    },
    submitBlog() {
      const blog_title = this.$refs.blog_title, form_file = this.$refs.form_file;
      const blog_title_feedback = this.$refs.blog_title_feedback, form_file_feedback = this.$refs.form_file_feedback;
      blog_title.classList.remove('is-valid');
      form_file.classList.remove('is-valid');
      blog_title.classList.remove('is-invalid');
      form_file.classList.remove('is-invalid');

      let form = document.getElementById('blog_form');
      let formData = new FormData(form);
      if(formData.get('blog_title') === "") {
        blog_title_feedback.innerText = "输入不能为空";
        blog_title.classList.add('is-invalid');
      }
      else if(formData.get('form_file').name === "") {
        form_file_feedback.innerText = "文件不能为空";
        form_file.classList.add('is-invalid');
      }
      else if(formData.get('form_file').name.slice(-3) !== ".md") {
        form_file_feedback.innerText = "文件类型错误";
        form_file.classList.add('is-invalid');
      }
      else {
        blog_title.value = "";
        form_file.value = "";
        blog_title.classList.add('is-valid');
        form_file.classList.add('is-valid');
        const path = `${this.httpUrl}/upload_blog`;
        axios.post(path, formData, {
          // headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: [function (data, headers) {
            // Do whatever you want to transform the data
            // console.log(headers.post)
            delete headers.post['Content-Type'];
            delete headers.get['Content-Type'];
            delete headers.common['Content-Type'];
            // console.log(headers.post)

            return data;
          }],
        })
          .then((res) => {
            if(res.data.status === "success")
              alert("上传成功！");
            else if(res.data.msg === "database_full")
              alert("服务器爆满！请删除一些博客文章，或者拓容~");
          })
          .catch((error) => {
            console.error(error);
          })
      }
    },
    submitAnnouncement() {
      const announcement_title = this.$refs.announcement_title, form_content = this.$refs.form_content;
      const announcement_title_feedback = this.$refs.announcement_title_feedback, form_content_feedback = this.$refs.form_content_feedback;
      announcement_title.classList.remove('is-valid');
      form_content.classList.remove('is-valid');
      announcement_title.classList.remove('is-invalid');
      form_content.classList.remove('is-invalid');

      let form = document.getElementById('announcement_form');
      let formData = new FormData(form);
      if(formData.get('announcement_title') === "") {
        announcement_title_feedback.innerText = "输入不能为空";
        announcement_title.classList.add('is-invalid');
      }
      else if(formData.get('form_content') === "") {
        form_content_feedback.innerText = "内容不能为空";
        form_content.classList.add('is-invalid');
      }
      else {
        announcement_title.value = "";
        form_content_feedback.value = "";
        form_content.value = "";
        announcement_title.classList.add('is-valid');
        form_content.classList.add('is-valid');
        const path = `${this.httpUrl}/upload_announcement`;
        axios.post(path, formData)
          .then((res) => {
            if(res.data.status === "success")
              alert("上传成功！");
          })
          .catch((error) => {
            console.error(error);
          })
      }
    },
  },
  created() {
    this.userStatus = jwtDecode(localStorage.token)
  },
  mounted() {
    let selected_tab = 2;
    const tabs = document.querySelectorAll(".tab");
    const tab_blocks = document.querySelectorAll(".tab-block")

    for(let i = 1; i <= tabs.length; i++) {
      if(i === selected_tab) {
        tabs[i - 1].classList.add("selected-tab")
        tab_blocks[i - 1].style.display = "block"
      }
      else
        tabs[i - 1].classList.add("not-selected-tab")

      tabs[i - 1].index = i
      tabs[i - 1].addEventListener("click", (e) => {
        let index = e.target.index
        if(index !== selected_tab) {
          tabs[selected_tab - 1].classList.remove("selected-tab")
          tabs[selected_tab - 1].classList.add("not-selected-tab")
          tab_blocks[selected_tab - 1].style.display = "none"

          selected_tab = index

          tabs[selected_tab - 1].classList.remove("not-selected-tab")
          tabs[selected_tab - 1].classList.add("selected-tab")
          tab_blocks[selected_tab - 1].style.display = "block"
        }
      })
    }
  },
  beforeRouteEnter(to, from, next) {
    if(localStorage.getItem('token') !== null)
      next()
    else
      console.log("请求被拦截")
      //this_.$router.push({ name: name })
  },
}
</script>

<style scoped>
.home {
  height: 100%;
  width: 100%;
  background-image: url("@/assets/imgs/index-background.jpg");
  background-size: cover;
  z-index: -1;
}
.block_background {
  background: rgba(255, 255, 255, 0.8);
}
.tab {
  height: 30px;
  line-height: 30px;
  margin-top: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
  overflow: hidden;
}
.not-selected-tab:hover {
  background-color: #f8f9fa;
  cursor: pointer;
}
.selected-tab {
  background-color: #6c757d;
  color: white;
}
.tab-block {
  display: none;
}
</style>