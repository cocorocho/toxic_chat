<template>
<div class="relative flex items-center justify-center
            h-12 w-12 mt-2 mb-2 mx-auto shadow-lg bg-gray-800
            text-green-500 hover:bg-green-600 hover:text-white
            rounded-3xl hover:rounded transition-all duration-300 ease-linear
            cursor-pointer"
            v-on:click="getChannelInfo">
    <h1>{{ name }}</h1>
</div>
</template>

<script>
import axios from "axios"

export default {
    name: "SidebarIcon",
    data() {
        return {
            url: ""
        }
    },
    methods: {
        async getChannelInfo() {
            try {
                let response = await axios.get(this.url)
                const data = response.data
                data["id"] = this.id
                this.$store.commit("switchToChannel", data)
            } catch (error) {
                console.log(error)
            }
        }
    },
    props: {
        name: {
            type: String,
            required: false
            },
        id: {
            type: Number,
            required: false
        }
    },
    created() {
        this.url = `channels/${this.id}/`
    }
}
</script>