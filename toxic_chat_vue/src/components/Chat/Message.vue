<template>
    <div class="my-2 bg-opacity-40 hover:bg-gray-400">
        <div class="mx-4">
            <div className="font-bold text-gray-300 text-sm">{{ author }}
                <span class="text-gray-500 text-xs">
                    - {{ date }}
                </span>
            </div>
            <div class="font-semibold text-white text-xs py-1">
                {{ content }}
            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: "Message",
    props: {
        author: String,
        content: String,
        date: Date
    }
}
</script>