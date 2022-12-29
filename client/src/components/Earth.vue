<template>
  <div class="home_earth">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">&#127759;访客</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <component :is="'script'" src="//rf.revolvermaps.com/0/0/6.js?i=5i4ejcytr5f&amp;m=7&amp;c=ff0000&amp;cr1=ffffff&amp;f=times_new_roman&amp;l=0" async="async"></component>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Earth",
  mounted() {
    let script = document.createElement('script')
    script.setAttribute('type', 'text/javascript')
    script.setAttribute('src', '//rf.revolvermaps.com/0/0/5.js?i=5qxsz5czulv&amp;m=0&amp;c=ff0000&amp;cr1=ffffff')
    script.setAttribute('async', 'async')
    document.head.appendChild(script)
  }
}
</script>

<style scoped>

</style>