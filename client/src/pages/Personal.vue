<template>
  <div class="container-fluid home"></div>
  <div class="container-fluid nav_personal">
    <div class="container text-start">
      <div class="row">
        <div class="col-3 block_background">
          <div class="container rounded-3 tab">个人中心</div>
          <div class="container rounded-3 tab">安全</div>
          <div v-if="userStatus != null && userStatus.authority === 3" class="container rounded-3 tab">发布博客</div>
        </div>
      </div>
    </div>
  </div>
  <div class="container text-start" style="padding-top: 50px">
    <div class="row">
      <div class="offset-3 col-9">
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
                          <input type="password" id="old_password" class="form-control">
                      </div>
                  </div>
                  <div class="row mb-3">
                      <div class="col-auto">
                          <label for="new_password" class="col-form-label">新密码</label>
                      </div>
                      <div class="col-auto">
                          <input type="password" id="new_password" class="form-control">
                      </div>
                  </div>
                  <div class="row mb-3">
                      <div class="col-auto">
                          <label for="new_password_2" class="col-form-label">再次输入新密码</label>
                      </div>
                      <div class="col-auto">
                          <input type="password" id="new_password_2" class="form-control">
                      </div>
                  </div>
                  <button type="submit" class="btn btn-outline-primary btn-sm">提交</button>
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

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Personal",
  data() {
    return {
      userStatus: null,
    }
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
        //this.$router.push({ name: name })
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
.nav_personal {
  padding-top: 50px;
  width: 100%;
  height: 100%;
  position: fixed;
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