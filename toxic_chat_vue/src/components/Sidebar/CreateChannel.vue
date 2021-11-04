<template>
<div class="relative flex items-center justify-center
            h-12 w-12 mt-2 mb-2 mx-auto shadow-lg bg-gray-800
            text-green-500 hover:bg-green-600 hover:text-white
            rounded-3xl hover:rounded transition-all duration-300 ease-linear
            cursor-pointer" v-on:click="createChannel">
    <i class="fas fa-plus fa-lg"></i>
</div>
</template>


<script>
import Swal from 'sweetalert2'
import axios from "axios"

export default {
    data() {
        return {

        }        
    },
    methods: {
        async createChannel() {
            const { value: channel_name } = await Swal.fire({
                title: 'Enter Channel Name',
                input: 'text',
                inputPlaceholder: '#channelname'
                })

            if (channel_name) {
                let url = "/channels/"
                let payload = {channel_name: channel_name}
                try {
                    let response = await axios.post(url, payload)
                    if (response.status === 201) {
                        location.reload()
                    }
                } catch (error) {
                }
            }
        }
    }
}
</script>