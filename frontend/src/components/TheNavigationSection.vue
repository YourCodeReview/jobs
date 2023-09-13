<template>
    <v-col cols="12" md="8" sm="12">
        <v-row>
            <v-col v-for="(item, index) in props.anchors" :key="index" class="py-1" cols="12" md="6" sm="6">
                <v-btn variant="text" :href="`https://yourcodereview.com/#${item.anchor}`">
                    {{ item.name }}
                </v-btn>
            </v-col>
            <v-col v-for="(link, index) in props.links" :key="index" class="py-1" cols="12" md="6" sm="6">
                <v-btn variant="text" :href="link.href">{{ link.name }}</v-btn>
            </v-col>
        </v-row>
    </v-col>
</template>

<script setup>
const props = defineProps({
    links: Array,
    anchors: Array,
})
</script>