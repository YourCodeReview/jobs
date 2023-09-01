<script setup>
import SvgLogo from './icons/SvgLogo.vue'

import { useStateStore } from '../stores/index'

const store = useStateStore()
</script>

<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-top">
                <div class="footer-top__left">
                    <div class="footer-top__logo">
                        <SvgLogo />
                    </div>
                    <div class="footer-top__contact">
                        <a class="footer-top__contact-email" href="mailto:yourcodereview@gmail.com">
                            yourcodereview@gmail.com
                        </a>
                        <a class="footer-top__contact-phone" href="tel:7499108276">
                            +7 (499) 110-82-76
                        </a>
                    </div>
                </div>
                <div class="footer-top__right">
                    <a href="https://mrqz.me/6400c6ab9c4e9c004d2fecfa"
                        >Тест "Возьмут ли меня в IT"</a
                    >
                    <ul class="footer-top__links">
                        <li
                            v-for="item in store.footerAnchors"
                            :key="item.name"
                            class="footer-top__link"
                        >
                            <a
                                :href="`https://yourcodereview.com/#${item.anchor}`"
                                target="_blank"
                                >{{ item.name }}</a
                            >
                        </li>
                    </ul>
                    <a href="https://blog.yourcodereview.com">Блог</a>
                </div>
            </div>
            <div class="footer-bottom"></div>
        </div>
    </footer>
</template>

<style scoped>
.footer {
    color: white;
    background-color: #070012;
}

.footer-container {
    display: flex;
    flex-direction: column;
}

.footer-top {
    display: flex;
    justify-content: space-between;
}

.footer-top__left {
    display: flex;
    flex-direction: column;
}

.footer-top__right {
    display: flex;
    align-items: start;
    justify-content: space-between;

    gap: 30px;
}

.footer-top__contact {
    display: flex;
    flex-direction: column;

    margin-top: auto;

    gap: 8px;
}

.footer-top__links {
    display: grid;

    padding: 0;

    list-style: none;

    grid-template-columns: repeat(2, min-content);
    grid-template-rows: repeat(4, 1fr);
    column-gap: 30px;
    row-gap: 10px;
}

@media screen and (max-width: 680px) {
    .footer-top {
        gap: var(--large-gap);
        flex-direction: column;
    }

    .footer-top__left {
        flex-direction: row;
        justify-content: space-between;
    }

    .footer-top__right {
        gap: var(--small-gap)
    }

    .footer-top__links {
        gap: var(--small-gap)
    }
}

@media screen and (max-width: 425px) {
    .footer-top__right {
        align-items: center;
        flex-direction: column;
    }

    .footer-top__left {
        align-items: center;
        flex-direction: column;
        gap: var(--medium-gap);
    }

    .footer-top__contact {
        align-items: center;
    }
    .footer-top__links {
        grid-template-columns: 1fr 1fr;
        text-align: center;
    }
}
</style>
