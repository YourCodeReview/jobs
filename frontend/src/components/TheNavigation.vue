<script setup>
const props = defineProps({
    links: Array,
});
</script>

<template>
    <v-btn
        class="px-1 mx-1 mx-lg-2"
        variant="text"
        v-for="link in props.links"
        :key="link.title"
        :href="link.url"
        :block="$vuetify.display.mdAndDown"
    >
        {{ link.title }}
    </v-btn>
</template>
