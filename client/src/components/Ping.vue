<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'
import global from '@/App'

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Ping",
  data() {
    return {
      msg: '哈哈',
      httpUrl: global.httpUrl,
    };
  },
  methods: {
    getMessage() {
      const path = `${this.httpUrl}/ping`
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created() {
    this.getMessage()
  }
}
</script>

<style scoped>

</style>