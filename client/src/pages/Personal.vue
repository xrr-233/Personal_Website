<template>
  <div class="container-fluid home position-fixed"></div>
  <div class="container text-start" style="padding-top: 50px">
    <div class="row g-1">
      <div class="col-3">
        <div class="row">
          <div class="container block_background" style="padding-top: 20px; padding-bottom: 20px">
            <div class="container rounded-3 tab"
                 @mouseenter="tabHover($event, 0)"
                 @mouseleave="tabHoverOff($event, 0)"
                 @click="tabClick($event, 0)">个人中心</div>
            <div class="container rounded-3 tab"
                 @mouseenter="tabHover($event, 1)"
                 @mouseleave="tabHoverOff($event, 1)"
                 @click="tabClick($event, 1)">安全</div>
            <div class="container rounded-3 tab"
                 @mouseenter="tabHover($event, 2)"
                 @mouseleave="tabHoverOff($event, 2)"
                 @click="tabClick($event, 2)"
                 v-if="userStatus != null && userStatus.authority === 3">管理员</div>
          </div>
        </div>
      </div>
      <div class="col-9">
        <div class="row">
          <div class="offset-1 col-10 block_background">
            <div class="row tab-block" v-if="currentTab === 0">
              <div class="container">
                <div class="container">

                </div>
              </div>
            </div>
            <div class="row tab-block" v-if="currentTab === 1">
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
            <div class="row tab-block" v-if="currentTab === 2">
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
                <div class="container pt-5">
                  <h4>更改背景</h4>
                  <hr>
                  <form id="announcement_form" @submit.prevent novalidate>
                    <div class="drag-area rounded-3 position-relative" @dragover="bgFileDragover" @drop="bgFileDrop">
                      <div v-if="bgFileName" class="file-name position-absolute top-50 start-50 translate-middle">
                        <img :src="bgFilePreview" :alt="bgFileName" height="175"/>
                      </div>
                      <div v-else class="uploader-tips position-absolute top-50 start-50 translate-middle">
                        <span>将背景图片拖拽至此，或</span>
                        <label for="fileInput" style="color: #11A8FF; cursor: pointer">点此上传</label>
                        <br />
                        仅支持PNG/JPG格式，文件大小不能超过10M
                        <br />
                        建议图片宽高比为16:9
                      </div>
                    </div>
                    <input type="file" id="fileInput" @change="bgFileUpload" style="display: none;">
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
      tabs: null,
      currentTab: 1,
      bgBatchFile: null,
      bgFileName: null,
      bgFilePreview: null,
      MAX_FILE_SIZE: 10 * 1024 * 1024,
    }
  },
  methods: {
    tabHover(e, id) {
      if(id !== this.currentTab) {
        e.currentTarget.style.backgroundColor = "#f8f9fa";
        e.currentTarget.style.cursor = "pointer";
      }
    },
    tabHoverOff(e, id) {
      if(id !== this.currentTab) {
        e.currentTarget.style.backgroundColor = "";
        e.currentTarget.style.cursor = "default";
      }
    },
    tabClick(e, id) {
      if(id !== this.currentTab) {
        this.tabs[this.currentTab].style.backgroundColor = "";
        this.tabs[this.currentTab].style.color = "black";
        this.currentTab = id;
        e.currentTarget.style.backgroundColor = "#6c757d";
        e.currentTarget.style.color = "white";
      }
    },
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
    bgFileIsValid(file) {
      if (!file) return;
      if (file.size > this.MAX_FILE_SIZE)
        return alert('文件大小不能超过10M！');
      if (file.type !== 'image/png' && file.type !== 'image/jpeg')
        return alert('请确认文件格式！');

      this.bgBatchFile = file;
      this.bgFileName = file.name;

      const reader = new FileReader();
      reader.readAsDataURL(file)
      const this_ = this;
      reader.onload = function () {
        this_.bgFilePreview = reader.result;
        console.log(this_.bgFilePreview);
      }
    },
    bgFileUpload (e) {
      const file = e.target.files.item(0);
      // 清空，防止上传后再上传没有反应
      e.target.value = ''
      return this.bgFileIsValid(file);
    },
    bgFileDragover (e) {
      e.preventDefault();
    },
    bgFileDrop (e) {
      e.preventDefault();
      const file = e.dataTransfer.files[0]; // 获取到第一个上传的文件对象
      return this.bgFileIsValid(file);
    },
    // https://blog.csdn.net/qq_1307495/article/details/111952900
  },
  created() {
    this.userStatus = jwtDecode(localStorage.token)
  },
  mounted() {
    this.tabs = document.querySelectorAll(".tab");

    this.tabs[this.currentTab].style.backgroundColor = "#6c757d";
    this.tabs[this.currentTab].style.color = "white";
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
  background-image: url("@/assets/imgs/index-background.png");
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
.drag-area {
  height: 200px;
  border: dashed 1px gray;
  margin-bottom: 10px;
  color: #777;
}
.uploader-tips {
  text-align: center;
}
</style>