<template>
  <!-- header -->
  <div class="header container-fluid">
    <div class="container text-center" style="line-height: 50px">
      <div class="row">
        <div class="col-1">
          <div class="mx-auto logo" @click="push('Index')"></div>
        </div>
        <router-link class="offset-2 col-1 header-tab" to="/gallery">作品</router-link>
        <router-link class="col-1 header-tab" to="/under_construction">空间</router-link>
        <router-link class="col-1 header-tab" to="/under_construction">工具</router-link>
        <router-link class="col-1 header-tab" to="/log">日志</router-link>
        <div class="offset-2 col-3 position-relative">
          <button class="btn dropdown-toggle" ref="login_tab" id="login_tab" data-toggle="dropdown" style="color: white">
            {{ userName }}
            <span class="caret"></span>
          </button>
          <div ref="login_side_block" id="login_side_block" class="shadow p-3 mb-5 bg-body rounded border border-1 border-secondary position-absolute top-100 start-50 translate-middle-x">
            <div class="container-fluid">
              <div v-if="userStatus === null">
                <button class="btn btn-outline-success col-12" data-bs-toggle="modal" data-bs-target="#login_modal">登录</button>
                <button class="btn btn-outline-primary col-12" @click="push('UnderConstruction')">注册</button>
              </div>
              <div v-else>
                <div class="row">
                  <div class="offset-2 col-4">
                    <img src="@/assets/imgs/xrr.jpg" alt="xrr" class="img-fluid rounded-circle">
                  </div>
                  <div class="col-4" style="line-height: 50px">
                    <b style="color: black">{{ userName }}</b>
                  </div>
                </div>
                <hr style="color: gray">
                <button class="btn btn-outline-secondary col-12" @click="block_toggle(); push('Personal')">个人中心</button>
                <button class="btn btn-outline-danger col-12" @click="logout()">退出登录</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="login_modal" tabindex="-1" aria-labelledby="modal_label" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="modal_label">登录</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form id="login_form">
            <div class="mb-5">
              <label for="email" class="col-form-label float-start">Email</label>
              <input type="text" class="form-control" id="email" name="email" aria-describedby="email_help">
              <div id="email_help" class="form-text text-danger float-start" style="display: none">用户名不存在</div>
            </div>
            <div class="mb-5">
              <label for="password" class="col-form-label float-start">密码</label>
              <input type="password" class="form-control" id="password" name="password" aria-describedby="password_help">
              <div id="password_help" class="form-text text-danger float-start" style="display: none">密码错误</div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" @click="login()">登录</button>
        </div>
      </div>
    </div>
  </div>
  <div class="footer container-fluid text-center">
    <p class="fw-light m-2">Portal</p>
    <div class="portal align-self-center">
      <a href="https://github.com/xrr-233" target="_blank"><div class="m-2 d-inline"><img src="@/assets/imgs/icon-github.png" alt="github"></div></a>
      <a href="https://space.bilibili.com/11254045" target="_blank"><div class="m-2 d-inline"><img src="@/assets/imgs/icon-bilibili.png" alt="bilibili"></div></a>
      <a href="https://www.zhihu.com/" target="_blank"><div class="m-2 d-inline"><img src="@/assets/imgs/icon-zhihu.png" alt="zhihu"></div></a>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Frame",
  data() {
    return {
      userName: '未登录',
      userStatus: null,
      login_block: null,
      login_tab: null,
    }
  },
  methods: {
    push(name) {
      this.$router.push({ name: name })
    },
    block_toggle() {
      if(this.userName === null)
        return
      if(this.login_block.style.display === "none")
        this.login_block.style.display = "block"
      else
        this.login_block.style.display = "none"
    },
    block_init() {
      this.login_block = this.$refs.login_side_block
      this.login_tab = this.$refs.login_tab
      this.login_block.style.display = "none"
      this.login_tab.addEventListener("click", this.block_toggle)
    },
    login() {
      let form = document.getElementById('login_form');
      let formData = new FormData(form);
      let email = document.getElementById('email_help');
      let password = document.getElementById('password_help');
      const path = `${this.httpUrl}/login`
      axios.post(path, formData)
        .then((res) => {
          if(res.data.status === "success") {

            localStorage.setItem('token', res.data.token);
            this.userStatus = jwtDecode(localStorage.token)
            if(this.userStatus.nickname !== null)
              this.userName = this.userStatus.nickname
            else
              this.userName = this.userStatus.user_name

            this.push("RefreshMedia")
            //this.block_toggle()

            /*let modal = document.getElementById('login_modal')
            let backdrop = document.querySelector('.modal-backdrop .fade .show')
            // Remove the `modal-open` class from the body
            document.body.classList.remove('modal-open')
            // Re-hide the modal from screen readers
            modal.setAttribute('aria-hidden', 'true')
            // Remove the `show` class from the backdrop
            backdrop.classList.remove('show')
            // Remove the `show` class from the modal
            modal.classList.remove('show')
            // Change the modal `display` style to `none`
            modal.style.display = 'none'
            // Remove the backdrop div from the body
            backdrop.remove();*/

            // location.reload()
          }
          else {
            email.style.display = "none"
            password.style.display = "none"
            if(res.data.msg === "user_not_exist")
              email.style.display = "block"
            else if(res.data.msg === "wrong_password")
              password.style.display = "block"
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    logout() {
      localStorage.removeItem('token')
      this.userName = '未登录'
      this.userStatus = null

      this.block_toggle()
      this.push('RefreshMedia')
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
        alert('你这个用户不乖哦~居然私自篡改token！不过我全部防出去，防出去了嗷（马保国并感')
        localStorage.removeItem('token')
      }
    }
  },
  mounted() {
    this.block_init()
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.header {
  position: fixed;
  background: black;
  color: white;
  height: 50px;
  z-index: 100;
}
.footer {
  position: fixed;
  bottom: 0;
  background: black;
  color: white;
  height: 5px;
  z-index: 100;
}
.footer:hover {
  animation: footer-hover 0.5s ease;
  animation-fill-mode: forwards;
}
@keyframes footer-hover
{
  from {height: 5px;}
  to {height: 100px;}
}
.logo {
  height: 50px;
  width: 50px;
  background-image: url("@/assets/imgs/logo.png");
}
.logo:hover {
  background-image: url("@/assets/imgs/logo-hover.png");
  cursor: pointer;
}
.header-tab {
  height: 50px;
  overflow: hidden;
  color: silver;
  text-decoration: none;
}
.header-tab:hover {
  background: linear-gradient(black 80%, grey);
  background-size: 100% 200%;
  height: 50px;
  animation: header-tab-hover 0.5s ease;
  animation-fill-mode: forwards;
  cursor: pointer;
}
.router-link-activated {
  background: white;
  color: black;
  height: 50px;
}
.router-link-activated:hover {
  background: white;
  color: black;
  height: 50px;
  animation: none;
  cursor: default;
}
#login_side_block {
  width: 100%;
  margin: 5px;
  display: none;
}
@keyframes header-tab-hover
{
  from {background-position: 0 75%; color: silver;}
  to {background-position: 0 100%; color: white;}
}
.portal img {
  width: 50px;
}
</style>