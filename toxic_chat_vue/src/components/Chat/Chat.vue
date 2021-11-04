<template>
<div className="ml-16 mt-16 h-screen w-screen rounded-xl">
    <!-- <Message
    :author="d"
    :content="b"
    />
    <Message
    :author="a"
    :content="b"
    /> -->
        
    <div v-if="currentChannelId" class="fixed bottom-0 left-0 h-16 w-screen flex items-center justify-center">
        <div class="bg-gray-600 rounded-xl w-9/12 h-10 flex justify-center">
            <input type="text" v-model="message" placeholder="Message here" v-on:keyup.enter="sendMessage"   class="bg-gray-600 w-4/5 focus:outline-none text-white">
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
        
        },
        currentChannelId() {
            return this.$store.state.currentChannel["id"]
        }
    },
    data() {
        return {
            message: "",
        }
    },
    methods: {
        async sendMessage() {
            const url = `/channels/${this.currentChannelId}/messages/`
            let vm = this
            try {
                if (vm.message.length) {
                    let payload = {"message": vm.message}
                    let response = await axios.post(url, payload)
                    console.log(response)
                }
                
            } catch (error) {
                
            }

        }
    }
}
</script>