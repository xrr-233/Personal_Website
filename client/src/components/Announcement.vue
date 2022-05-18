<template>
  <div class="home_announcement">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">&#128226;公告栏</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><div class="text">我一定要写出网页！</div></td>
        </tr>
        <tr>
          <td><div class="text">该死的阿里云赶快给我认证通过！</div></td>
        </tr>
        <tr><td><div class="text">&nbsp;</div></td></tr>
        <tr><td><div class="text">&nbsp;</div></td></tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Announcement"
}
</script>

<style scoped>
.text {
  float: left;
}
</style>