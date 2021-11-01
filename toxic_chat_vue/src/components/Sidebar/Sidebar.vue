<template>
<div className="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg">
    <SidebarIcon
    v-for="channel in channels" :key="channel"
    :name="channel.name[0]"
    :id="channel.id"
    />
</div>
    
</template>

<script>
import axios from "axios"
import SidebarIcon from "./SidebarIcon.vue"

export default {
    name: "Sidebar",
    data() {
        return {
            channels: []
        }
    },
    components: {
        SidebarIcon
    },
    methods: {
        async getChannels() {
            const url = "/channels/"
            const vm = this
            try {
                let response = await axios.get(url)
                const resp_channels = response.data["channels"]
                for (let i=0; i < resp_channels.length; i++) {
                    vm.channels.push(resp_channels[i])
                }
            } catch (error) {
                console.log(error)
            }
        }
    },
    created() {
        this.getChannels()
    }
}
</script>