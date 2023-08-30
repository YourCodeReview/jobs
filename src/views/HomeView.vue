<script setup>
import TheJobsList from '../components/TheJobsList.vue'
import { useStateStore } from '../stores/index'

const store = useStateStore()
</script>

<template>
    <main class="job">
        <div class="job-nav">
            <!-- <div class="nav__tools"></div> -->
            <div class="nav__jobs">
                <TheJobsList :jobs="store.vacancies" />
            </div>
        </div>
    </main>
</template>

<style scoped>
.job {
    flex: auto;
}

.job-nav {
    display: grid;

    max-width: 1280px;
    margin: 0 auto;
    padding: 40px 28px;
    /* grid-template-columns: 288px 1fr; */

    grid-template-columns: 1fr;
    grid-gap: 24px;
}
</style>
