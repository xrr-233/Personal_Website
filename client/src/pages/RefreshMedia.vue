<template>
  <div></div>
</template>

<script>
export default {
  name: "RefreshMedia",
  beforeRouteEnter(to, from, next) {
    let from_name = from.name
    if(from_name === undefined)
      from_name = "Index"
    next((vm) => {
      vm.$router.push({
        name: from_name
      })
    })
  }
}
</script>

<style scoped>

</style>