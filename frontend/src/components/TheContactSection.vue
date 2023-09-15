<template>
  <v-col cols="12" md="4" sm="12" class="d-flex flex-column py-1">
    <v-btn class="justify-start" variant="text" href="https://yourcodereview.com"
      >&#60; codereview &#47;&#62;</v-btn
    >
    <div class="mt-auto">
      <v-btn
        v-for="contact in props.contacts"
        :key="contact.name"
        class="justify-start"
        variant="text"
        :href="contact.href"
        block
        >{{ contact.name }}</v-btn
      >
    </div>
  </v-col>
</template>

<script setup>
const props = defineProps({
  contacts: Array
})
</script>
