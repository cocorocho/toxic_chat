<template>
<div className="ml-16 mt-16 h-screen w-screen rounded-xl">
    <Message
    :author="a"
    :content="b"
    />
    <Message
    :author="a"
    :content="b"
    />
    
    
    <div class="fixed bottom-0 left-0 h-16 w-screen flex items-center justify-center">
        <div class="bg-gray-600 rounded-xl w-9/12 h-10 flex justify-center">
            <input type="text" placeholder="Message here" class="bg-gray-600 w-4/5 focus:outline-none text-white">
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios"
import Message from "./Message.vue"


export default {
    name: "Chat",
    components: {
        Message
    },
    computed: {
        getMessages() {

        }
    },
    data() {
        return {
            a: "ADMIN",
            b: "HELLO WORLD"
        }
    },
    methods: {
        async sendMessage() {
            const channel_id = this.$store.state.currentChannel
            const url = ``
        }
    }
}
</script>