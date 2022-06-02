<template>
  <div class="container-fluid home position-fixed"></div>
  <div class="container text-start" style="padding-top: 50px">
    <div class="row">
      <div class="col-3 block_background">
          <div class="container rounded-3 tab">个人中心</div>
          <div class="container rounded-3 tab">安全</div>
          <div v-if="userStatus != null && userStatus.authority === 3" class="container rounded-3 tab">发布博客</div>
      </div>
      <div class="col-9">
        <div class="container">
          <div class="row tab-block">
            <div class="col-12 block_background">
              <div class="container">

              </div>
            </div>
          </div>
          <div class="row tab-block">
            <div class="col-12 block_background">
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
          <div class="row tab-block">
            <div class="col-12 block_background">
                <div class="container pt-5">
                    <h4>发布博客</h4>
                    <hr>
                    <form id="blog_form" method="post" enctype="multipart/form-data" onsubmit="submit_blog(); return false">
                        <div class="mb-3">
                            <label for="blog_title" class="form-label">博客标题</label>
                            <input class="form-control" type="text" id="blog_title" name="blog_title">
                        </div>
                        <div class="mb-3">
                            <label for="form_file" class="form-label">请上传markdown(.md)文件</label>
                            <input class="form-control" type="file" id="form_file" name="form_file" accept=".md">
                        </div>
                        <button type="submit" class="btn btn-outline-primary btn-sm">提交</button>
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
</template>

<script>
import jwtDecode from "jwt-decode";
import axios from "axios";
import global from "@/App";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Personal",
  data() {
    return {
      httpUrl: global.httpUrl,
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
              this.$refs.old_password.value = ""
              this.$refs.new_password.value = ""
              this.$refs.new_password2.value = ""
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
    }
  },
  created() {
    this.userStatus = jwtDecode(localStorage.token)
  },
  mounted() {
    /*let this_ = this
    this_.screenWidth = window.innerWidth
    this_.screenHeight = window.innerHeight
    this_.scrollY = window.scrollY
    window.onresize = () => {
      this_.screenWidth = window.innerWidth
      this_.screenHeight = window.innerHeight
    }
    window.onscroll = () => {
      this_.scrollY = window.scrollY
    }*/

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

    /*function submit_blog() {
        var formData = new FormData(document.getElementById('blog_form'));
        console.log(formData.get('form_file'));
        $.ajax({
            url: "{{ url_for('personal.upload_blog') }}",
            type: "POST",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            dataType: 'json',
            success: function(e) {
                alert(e['status']);
            },
            error: function() {
                console.log('服务器内部出错');
            }
        });
    }*/
  },
  beforeRouteEnter(to, from, next) {
    if(localStorage.getItem('token') !== null)
      next()
    else
      console.log("请求被拦截")
      //this_.$router.push({ name: name })
  },
  deactivated() {
    this.$refs.old_password.value = ""
    this.$refs.new_password.value = ""
    this.$refs.new_password2.value = ""
    this.$refs.old_password.classList.remove('is-invalid')
    this.$refs.new_password.classList.remove('is-invalid')
    this.$refs.new_password2.classList.remove('is-invalid')
  }
}
</script>

<style scoped>
.home {
  height: 100%;
  width: 100%;
  background-image: url("../../public/index-background.jpg");
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