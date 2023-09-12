<script setup>
const props = defineProps({
    links: Array,
});
</script>

<template>
    <v-btn
        v-for="link in props.links"
        :key="link.title"
        class="px-1 mx-1"
        height="50"
        variant="text"
        rounded="lg"
        :href="link.url"
        :block="$vuetify.display.mdAndDown"
    >
        {{ link.title }}
    </v-btn>
</template>
