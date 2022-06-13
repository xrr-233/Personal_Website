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

export default {
  name: "App",
  components: { Frame },
  provide() {
    return {
      httpUrl: '***',
    }
  },
  mounted() {
    /*const ap = */
    new APlayer({
      container: this.$refs.a_player,
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

<style scoped>

</style>
