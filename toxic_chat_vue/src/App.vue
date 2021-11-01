<template>
  <div className="flex min-h-screen bg-gray-700">
    <router-view/>
  </div>
</template>

<style>
</style>

<script>
export default {
  beforeCreate() {
    this.$store.commit("initialize")
  }
}
</script>