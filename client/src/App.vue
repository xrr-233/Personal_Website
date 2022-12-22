<template>
  <frame></frame>
  <!--<router-view v-slot="{ Component }">
    <keep-alive>
      <component :is="Component" />
    </keep-alive>
  </router-view>-->
  <router-view></router-view>
  <div ref="a_player"></div>
</template>

<script>
import Frame from "@/components/Frame";
import APlayer from "aplayer"
import 'aplayer/dist/APlayer.min.css'
import axios from "axios";

export default {
  name: "App",
  components: { Frame },
  data() {
    return {
      httpUrl: 'http://***:***',
      musicPlayer: null,
    }
  },
  provide() {
    return {
      httpUrl: this.httpUrl,
    }
  },
  mounted() {
    this.musicPlayer = new APlayer({
      container: this.$refs.a_player,
      fixed: true,
      listFolded: false,
    })
    const path = `${this.httpUrl}/get_music_list`;
    axios.get(path)
        .then((res) => {
          let musicList = res.data.music_list;
          for (let i = 0; i < musicList.length; i++) {
            this.musicPlayer.list.add({
              name: musicList[i].name,
              artist: musicList[i].artist,
              url: `${this.httpUrl}/get_music/${musicList[i].key}`,
              // cover: '{{ url_for('static', filename='images/TOKIMEKI Runners.jpg') }}',
              // theme: '#ffaec9'
            })
          }
          this.musicPlayer.play();
        })
        .catch((error) => {
          console.error(error)
          this.blogs_num = null
        })
  }
}
</script>

<style scoped>

</style>
