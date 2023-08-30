<script setup>
import { computed } from 'vue'
import UiButton from './ui/UiButton.vue'
import SvgLogo from './icons/SvgLogo.vue'

const emits = defineEmits(['openModalType', 'logout'])

const props = defineProps({
    links: {
        type: Array
    },
    user: {
        type: Object
    },
    isLoggedIn: {
        type: Boolean
    }
})

const userPhoto = computed(() => props.user?.photoURL)
const userName = computed(() => props.user?.displayName)

const openModalType = (status) => {
    emits('openModalType', status)
}

const logout = () => {
    emits('logout')
}
</script>

<template>
    <nav class="nav">
        <router-link class="nav-logo" to="/">
            <SvgLogo />
            Jobs
        </router-link>
        <div class="nav-links">
            <a v-for="(link, idx) in props.links" :href="link.url" :key="idx" target="_blank">
                {{ link.title }}
            </a>
            <div v-if="userName && userPhoto" class="user-info">
                <img class="user-image" :src="userPhoto" alt="user-image" />
                <span class="user-name">{{ userName }}</span>
            </div>
            <UiButton v-if="props.isLoggedIn" text="Выйти" @click="logout" />
            <template v-else>
                <UiButton text="Войти" @click="openModalType('login')" />
                <UiButton
                    text="Зарегистрироваться"
                    color="black"
                    @click="openModalType('register')"
                />
            </template>
        </div>
    </nav>
</template>

<style scoped>
.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;

    min-height: 72px;
    max-height: 72px;
}

.nav-logo {
    display: flex;
    align-items: center;

    color: white;

    font-size: 20px;

    gap: 10px;
}
.nav-links {
    display: flex;
    align-items: center;

    color: white;

    gap: 20px;
}
.user-info {
    display: flex;
    align-items: center;

    gap: 10px;
}
.user-image {
    width: 32px;
    height: 32px;

    border-radius: 50%;
}
</style>
