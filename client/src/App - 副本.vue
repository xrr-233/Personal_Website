<template>
  <!-- header -->
  <div class="header container-fluid">
    <div class="container text-center" style="line-height: 50px">
      <div class="row">
        <div class="col-1">
          <div class="mx-auto logo" @click="jump('/')"></div>
        </div>
        <div class="offset-2 col-1 header-tab" @click="jump('/under_construction')">博客</div>
        <div class="col-1 header-tab" @click="jump('/under_construction')">作品</div>
        <div class="col-1 header-tab" @click="jump('/under_construction')">空间</div>
        <div class="col-1 header-tab" @click="jump('/under_construction')">工具</div>
        <div class="offset-2 col-3 position-relative">
          <button class="btn dropdown-toggle" ref="login_tab" id="login_tab" data-toggle="dropdown" style="color: white">
            {{ user }}
            <span class="caret"></span>
          </button>
          <div ref="login_side_block" id="login_side_block" class="shadow p-3 mb-5 bg-body rounded border border-1 border-secondary position-absolute top-100 start-50 translate-middle-x">
            <div class="container-fluid">
              <div v-if="user === '未登录'">
                <button class="btn btn-outline-success col-12" data-bs-toggle="modal" data-bs-target="#login_modal">登录</button>
                <button class="btn btn-outline-primary col-12">注册</button>
              </div>
              <div v-else>
                <div class="row">
                    <div class="offset-2 col-4">
                        <img src="./assets/xrr.jpg" alt="xrr" class="img-fluid rounded-circle">
                    </div>
                    <div class="col-4" style="line-height: 50px">
                        <b style="color: black">{{ user }}</b>
                    </div>
                </div>
                <hr style="color: gray">
                <button class="btn btn-outline-secondary col-12">个人中心</button><!-- onclick="location.href='{{ url_for("personal.personal") }}'" -->
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
  <router-view/>
  <div ref="a_player"></div>
</template>

<script>
/*
var images = new Array()
function preload() {
    for (var i = 0; i < preload.arguments.length; i++) {
        images[i] = new Image()
        images[i].src = preload.arguments[i]
    }
}
preload(
    "../images/logo.png",
    "../images/logo-hover.png"
)
*/
import axios from "axios"
import APlayer from "aplayer"
import 'aplayer/dist/APlayer.min.css'

const httpUrl = '***'

export default {
  name: "App",
  httpUrl,
  data() {
    return {
      user: null,
      userStatus: null,
    }
  },
  methods: {
    getUserStatus() {
      const path = `${httpUrl}/get_user_status`
      axios.get(path)
        .then((res) => {
          if(res.data.user == null) {
            this.user = "未登录"
            this.userStatus = null
          }
          else {
            if(res.data.user.nickname !== null)
              this.user = res.data.user.nickname
            else
              this.user = res.data.user.user_name
            this.userStatus = res.data.user
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    jump(path){
      this.$router.push({ path: path })
      //this.$router.go(-2)
      //后退两步
    },
    login() {
      let form = document.getElementById('login_form');
      let formData = new FormData(form);
      let email = document.getElementById('email_help');
      let password = document.getElementById('password_help');
      const path = `${httpUrl}/login`
      axios.post(path, formData)
        .then((res) => {
          if(res.data.status === "success") {
            location.reload()
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
      const path = `${httpUrl}/logout`
      console.log(this.userStatus)
      axios.post(path, this.userStatus)
        .then((res) => {
          if(res.data.status === "success") {
            location.reload()
          }
          else {
            console.error(res)
          }
        })
        .catch((error) => {
          console.error(error)
        })
    /*
        $.ajax({
            url: "{{ url_for('index.logout') }}",
            type: "GET",
            dataType: 'json',
            success: function(e) {
                if(e.status === "success") {
                    location.href = "{{ url_for("index.index") }}";
                }
            },
            error: function() {
                alert('500 服务器内部问题，加载失败');
            }
        });
    */
    },
  },
  created() {
    this.getUserStatus()
  },
  mounted() {
    const this_ = this
    const login_block = this.$refs.login_side_block
    const login_tab = this.$refs.login_tab
    login_block.style.display = "none"
    login_tab.addEventListener("click", function() {
      if(this_.user === null)
        return
      if(login_block.style.display === "none")
        login_block.style.display = "block"
      else
        login_block.style.display = "none"
    })

    /*const ap = */
    new APlayer({
      container: this_.$refs.a_player,
      fixed: true,
      autoplay: true,
      /*audio: [
        {
            name: 'TOKIMEKI Runners',
            artist: '虹ヶ咲学園スクールアイドル同好会',
            url: 'https://music.163.com/#/song?id=1327263602',
            cover: '{{ url_for('static', filename='images/TOKIMEKI Runners.jpg') }}',
            theme: '#ffaec9'
        }
      ]*/
    })
  }
}
</script>

<style>
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
    z-index: 1;
}
.logo {
    height: 50px;
    width: 50px;
    background-image: url("../public/logo.png");
}
.logo:hover {
    background-image: url("../public/logo-hover.png");
    cursor: pointer;
}
.header-tab {
    height: 50px
}
.header-tab:hover {
    background: linear-gradient(black 80%, grey);
    background-size: 100% 200%;
    height: 50px;
    animation: header-tab-hover 0.5s ease;
    animation-fill-mode: forwards;
    cursor: pointer;
}
.header-tab-pressed {
    background: white;
    color: black;
    height: 50px;
}
#login_side_block {
    width: 100%;
    margin: 5px;
    display: none;
}
@keyframes header-tab-hover
{
    from {background-position: 0 0;}
    to {background-position: 0 100%;}
}
</style>
