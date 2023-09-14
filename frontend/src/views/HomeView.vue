<script setup>
import TheWelcomeForm from '@/components/TheWelcomeForm.vue';
import { onMounted } from 'vue';


onMounted(() => {
    console.log('hello');
})
</script>

<template>
    <div class="text-white">
        <the-welcome-form />
    </div>
</template>
