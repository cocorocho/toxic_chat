<template>
<Sidebar/>
<Topbar/>
<Chat/>
</template>


<script>
import axios from "axios"
import Sidebar from "@/components/Sidebar/Sidebar.vue"
import Chat from "@/components/Chat/Chat.vue"
import Topbar from "@/components/Topbar.vue"

export default {
    setup() {
    },
    components: {
        Sidebar,
        Topbar,
        Chat,
    },
    beforeCreate() {
        if (!this.$store.state.isAuthenticated) {
            this.$router.push("/login/")
        }
    }
}
</script>