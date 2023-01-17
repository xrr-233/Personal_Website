<template>
  <div class="home_announcement">
    <table class="table" style="table-layout:fixed;">
      <thead>
        <tr><th scope="col">&#128226;公告</th></tr>
      </thead>
      <tbody>
        <tr v-if="announcements_num === 0"><td><div class="text">暂无公告</div></td></tr>
        <tr v-else v-for="announcement in announcements" :key="announcement.announcement_title">
          <td>
            <div class="announcement text fw-bold" v-on:click="chooseAnnouncement(announcement.id)">
              <u>{{ announcement.announcement_title }}</u>
            </div>
          </td>
        </tr>
        <tr v-if="announcements_num > max_title_num"><td><div class="fw-bold">查看更多</div></td></tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  inject: ["httpUrl"],
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Announcement",
  data() {
    return {
      announcements_num: 0,
      announcements: [],
      max_title_num: 4,
    }
  },
  methods: {
    askForAnnouncementTitles() {
      const path = `${this.httpUrl}/get_announcement_titles`
      axios.post(path, {
        'max_title_num': this.max_title_num,
      })
        .then((res) => {
          if(res.data.error === null) {
            this.announcements_num = res.data.number;
            this.announcements = res.data.announcements;
          }
          else {
            this.announcements_num = null
          }
        })
        .catch((error) => {
          console.error(error)
          this.announcements_num = null
        })
    },
    chooseAnnouncement(id) {
      this.$router.push({ path: `/announcement/${id}` })
    },
  },
  mounted() {
    this.askForAnnouncementTitles();
  }
}
</script>

<style scoped>
td {
  text-align: left;
  overflow: hidden;
  white-space: nowrap;
}
.announcement:hover {
  color: blue;
  cursor: pointer;
}
</style>