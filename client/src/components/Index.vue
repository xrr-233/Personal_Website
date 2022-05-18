<template>
  <div class="container-fluid home">
    <div class="container">
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
  <div class="container" style="padding-top: 50px">
    <div class="offset-3 col-6">
      <div class="row">
        <div class="offset-1 col-10 block_background">
          <div class="container">
            <table class="table">
              <thead>
                <tr>
                    <th scope="col">&#127774;博客</th>
                </tr>
              </thead>
              <tbody id="index_blog_list" ref="index_blog_list"></tbody>
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
import global from "@/App";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Index",
  components: {Divination, ClockMaster, Announcement},
  data() {
    return {
      tr: "",
      httpUrl: global.httpUrl,
    }
  },
  methods: {
    askForBlogs(start_page, per_page) {
      let tr = "";
      const path = `${this.httpUrl}/ask_for_blogs`
      axios.post(path, {
        'start_page': start_page,
        'per_page': per_page
      })
        .then((res) => {
          if(res.data.error === null) {
            for(let i = 0; i < res.data.number; i++) {
              let blog = res.data.blogs[i]
              tr += ` \
                <tr> \
                  <td style="padding: 30px 0"> \
                    <p class="fs-1 fw-bold">${blog.blog_title}</p> \
                    <div class="blog" style="text-align: left"> \
                      ${marked.parse(blog.content)} \
                    </div> \
                    <p class="fs-6 fw-light text-secondary" style="text-align: right">发布于 ${blog.create_time}</p>
                  </td> \
                </tr> \
              `
            }
          }
          else
            tr += "<tr><td>服务器内部错误</td></tr>"
          this.tr = tr
          this.$refs.index_blog_list.innerHTML = this.tr
        })
        .catch((error) => {
          console.error(error)
          tr += "<tr><td>服务器内部错误</td></tr>"
          this.tr = tr
          this.$refs.index_blog_list.innerHTML = this.tr
        })
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
</style>