<template>
  <v-hover v-slot="{ isHovering, props }">
    <v-card
      v-bind="props"
      class="py-4 mx-auto mb-4"
      :class="`card-${size}`"
      :elevation="isHovering && size === 'md' ? 10 : 1"
      rounded="xl"
    >
      <v-card-subtitle class="font-weight-bold">{{ item?.company }}</v-card-subtitle>
      <v-card-title
        v-if="item.title"
        class="font-weight-bold"
        :class="size === 'lg' ? 'text-h5' : ''"
        >{{ item.title }}</v-card-title
      >
      <v-chip-group class="custom-chips">
        <v-chip
          v-if="item.employment"
          class="chip text-grey-darken-2"
          prepend-icon="mdi-briefcase"
          label
          >{{ item.employment }}</v-chip
        >

        <v-chip
          v-if="item.address"
          class="chip text-grey-darken-2"
          prepend-icon="mdi-map-marker"
          label
          >{{ item.address.split(',')[0] }}</v-chip
        >

        <v-chip
          v-if="item.salary && size !== 'lg'"
          class="chip chip-salary text-grey-darken-2"
          label
          >неверный формат salary</v-chip
        >
      </v-chip-group>
    </v-card>
  </v-hover>
</template>

<script setup>
defineProps({
  item: Object,
  size: {
    type: String,
    default: 'md'
  }
})
</script>

<style scoped>
.card-md {
  max-width: 600px;
}
.card-lg {
  max-width: 100%;
}
.custom-chips {
  padding: 0.5rem 1rem;
}

.card-md .chip-salary {
  margin-left: 0;
}

@media screen and (min-width: 1280px) {
  .card-md .chip-salary {
    margin-left: auto;
  }
}
</style>
