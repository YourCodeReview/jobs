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
        <div class="nav-tools">
            <div class="nav-tools__links">
                <a v-for="(link, idx) in props.links" :href="link.url" :key="idx" target="_blank">
                    {{ link.title }}
                </a>
            </div>
            <div class="nav-tools__buttons">
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
        </div>
    </nav>
</template>

<style scoped>
.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--large-gap);
}

.nav-logo {
    display: flex;
    align-items: center;

    color: white;

    font-size: 20px;

    gap: var(--small-gap);
}

.nav-tools {
    display: flex;
    align-items: center;
    gap: var(--large-gap);
}
.nav-tools__links {
    display: flex;
    align-items: center;

    color: white;

    gap: var(--medium-gap);
}

.nav-tools__buttons {
    display: flex;
    align-items: center;
    gap: var(--small-gap);
}
.user-info {
    display: flex;
    align-items: center;

    gap: var(--small-gap);
}
.user-image {
    width: 32px;
    height: 32px;

    border-radius: 50%;
}

.user-name {
    color: white;
}

@media screen and (max-width: 975px) {
    .nav-tools {
        flex-direction: column;
        gap: var(--small-gap)
    }
}

@media screen and (max-width: 680px) {

    .nav {
        flex-direction: column;
        gap: var(--medium-gap);
    }
}
</style>
