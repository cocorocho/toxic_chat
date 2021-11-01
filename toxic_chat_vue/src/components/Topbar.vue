<template>
    <div class="fixed top-0 w-screen bg-gray-800 text-white ml-16 h-16 flex items-center px-2 text-xl font-extrabold">
        <span>{{ channelName }}</span>
        <span v-on:click="logout" class="fixed right-4 font-medium hover:text-green-400 transition-all duration-500 cursor-pointer">Logout</span>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "Topbar",
    computed: {
        channelName() {
            if (Object.keys(this.$store.state.currentChannel).length) {
                return `# ${this.$store.state.currentChannel["name"]}`
            }
        }
    },
    methods: {
        async logout() {
            if (this.$store.state.isAuthenticated) {
                try {
                    let response = await axios.get("/logout/")
                    this.$store.commit("removeToken")
                    if (localStorage.getItem("token")) {
                        localStorage.removeItem("token")
                    }
                    this.$router.push("/login/")
                } catch (error) {
                    console.error(error)                    
                }
            }
        }
    }
}
</script>