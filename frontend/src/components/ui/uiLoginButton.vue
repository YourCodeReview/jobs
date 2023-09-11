<template>
    <v-btn
        class="mx-1 mx-lg-2"
        height="50"
        rounded="lg"
        :variant="variant"
        :block="block"
        :to="{
            path: '/login',
            query: { type: 'login' },
        }"
    >
        Войти
    </v-btn>
</template>

<script setup>
defineProps({
    variant: String,
    block: Boolean
})
</script>