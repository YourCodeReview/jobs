<script setup>
import SvgRemote from '../icons/SvgRemote.vue'
import SvgLocation from '../icons/SvgLocation.vue'

const props = defineProps({
    job: Object,
    size: {
        type: String,
        default: 'medium'
    }
})
</script>

<template>
    <div class="card" :class="`card__${props.size}`">
        <router-link :to="`/vacancy/${props.job.id}`">
            <div v-if="props.size === 'medium'" class="card-top">
                <p class="card-top__company">{{ props.job.company_name }}</p>
            </div>
            <div class="card-btm">
                <h3 class="card-btm__title">{{ props.job.vacancy_name }}</h3>
                <div class="card-btm__info">
                    <span class="info-span">
                        <SvgLocation />
                        {{ props.job.location }}
                    </span>
                    <span v-if="props.job.remote" class="info-span">
                        <SvgRemote />
                        Удаленно
                    </span>
                    <span v-if="props.size === 'medium'" class="info-span info-span__salary">
                        {{ props.job.salary }} ₽
                    </span>
                </div>
            </div>
        </router-link>
    </div>
</template>

<style scoped>
.card {
    position: relative;

    overflow: hidden;

    width: 100%;
    max-width: 600px;

    transition: all 0.3s ease;

    border-radius: 12px;
    background: white;
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.03),
        0px 16px 28px rgba(0, 0, 0, 0.04),
        0px 2px 10px rgba(0, 0, 0, 0.02),
        0px 0px 1px rgba(0, 0, 0, 0.04);
}

.card__large {
    max-width: 100%;
}

.card__large .card-btm__title {
    font-size: 28px;
}

.card:hover {
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.06),
        0px 16px 28px rgba(0, 0, 0, 0.07),
        0px 2px 10px rgba(0, 0, 0, 0.05),
        0px 0px 1px rgba(0, 0, 0, 0.06);
}

.card-top {
    padding: 16px 16px 5px;
}

.card-btm {
    padding: 16px;
}

.card-btm__title {
    overflow: hidden;

    max-height: 72px;
    margin-bottom: 20px;

    letter-spacing: -0.005em;

    font-size: 20px;
    font-weight: 700;
    line-height: 120%;
}

.card-btm__info {
    display: flex;
    align-items: center;
    justify-content: start;

    gap: 5px;
}
.info-span {
    display: flex;
    align-items: center;

    min-height: 30px;
    max-height: 30px;
    padding: 8px;

    white-space: nowrap;

    border-radius: 6px;
    background: #f7f7f7;

    gap: 5px;
}
.info-span svg {
    color: #a6a6a6;
}

.info-span__salary {
    margin-left: auto;
}

@media screen and (max-width: 425px) {
    .card-top {
        padding: 10px 10px 5px;
    }
    .card-btm {
        padding: 5px 10px;
    }

    .card-btm__title {
        margin-bottom: 10px;
    }

    .card-btm__info {
        align-items: start ;
        flex-direction: column;
    }

    .info-span__salary {
        margin-left: 0;
    }

    .info-span {
        padding: 5px;
    }
}
</style>
