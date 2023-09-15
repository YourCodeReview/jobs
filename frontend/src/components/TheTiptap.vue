<template>
  <div class="border mb-6">
    <div v-if="editor" class="d-flex flex-wrap">
      <v-btn
        icon="mdi-format-header-2"
        rounded="0"
        variant="flat"
        @click="toggleHeading(2)"
        :active="isActive('heading', { level: 2 })"
      >
      </v-btn>
      <v-btn
        icon="mdi-format-bold"
        rounded="0"
        variant="flat"
        @click="toggleBold"
        :disabled="!canToggleBold()"
        :active="isActive('bold')"
      >
      </v-btn>
      <v-btn
        icon="mdi-format-italic"
        rounded="0"
        variant="flat"
        @click="toggleItalic"
        :disabled="!canToggleItalic()"
        :active="isActive('italic')"
      >
      </v-btn>
      <!-- <v-btn icon="mdi-format-header-1" size="small" rounded="0" variant="flat" @click="toggleHeading(1)" :active="isActive('heading', { level: 1 })">
      </v-btn> -->
      <!-- <v-btn icon="mdi-format-header-3" size="small" rounded="0" variant="flat" @click="toggleHeading(3)" :active="isActive('heading', { level: 3 })">
      </v-btn>
      <v-btn icon="mdi-format-header-4" size="small" rounded="0" variant="flat" @click="toggleHeading(4)" :active="isActive('heading', { level: 4 })">
      </v-btn>
      <v-btn icon="mdi-format-header-5" size="small" rounded="0" variant="flat" @click="toggleHeading(5)" :active="isActive('heading', { level: 5 })">
      </v-btn>
      <v-btn icon="mdi-format-header-6" size="small" rounded="0" variant="flat" @click="toggleHeading(6)" :active="isActive('heading', { level: 6 })">
      </v-btn> -->
      <v-btn
        icon="mdi-format-list-bulleted"
        rounded="0"
        variant="flat"
        @click="toggleBulletList"
        :active="isActive('bulletList')"
      >
      </v-btn>
      <v-btn
        icon="mdi-format-list-numbered"
        rounded="0"
        variant="flat"
        @click="toggleOrderedList"
        :active="isActive('orderedList')"
      >
      </v-btn>
    </div>
    <editor-content :editor="editor" />
  </div>
</template>

<script setup>
import StarterKit from '@tiptap/starter-kit'
import { Editor, EditorContent } from '@tiptap/vue-3'

import { ref, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    required: true
  }
})
const emits = defineEmits(['update:modelValue'])
const editor = ref(null)

onMounted(() => {
  editor.value = new Editor({
    extensions: [StarterKit],
    content: props.modelValue,
    onUpdate: () => {
      emits('update:modelValue', editor.value.getHTML())
    }
  })
})

onBeforeUnmount(() => {
  editor.value.destroy()
})

const isActive = (command, params = {}) => {
  return editor.value.isActive(command, params)
}
const toggleBold = () => {
  editor.value.chain().focus().toggleBold().run()
}
const canToggleBold = () => {
  return editor.value.can().chain().focus().toggleBold().run()
}
const toggleItalic = () => {
  editor.value.chain().focus().toggleItalic().run()
}
const canToggleItalic = () => {
  return editor.value.can().chain().focus().toggleItalic().run()
}
const toggleHeading = (level) => {
  editor.value.chain().focus().toggleHeading({ level }).run()
}
const toggleBulletList = () => {
  editor.value.chain().focus().toggleBulletList().run()
}
const toggleOrderedList = () => {
  editor.value.chain().focus().toggleOrderedList().run()
}
// const undo = () => {
//   editor.value.chain().focus().undo().run();
// };
// const canUndo = () => {
//   return editor.value.can().chain().focus().undo().run();
// };
// const redo = () => {
//   editor.value.chain().focus().redo().run();
// };
// const canRedo = () => {
//   return editor.value.can().chain().focus().redo().run();
// };

onBeforeUnmount(() => {
  editor.value.destroy()
})
</script>

<style>
.tiptap {
  min-height: 200px;
  margin-top: 0.75em;
  margin-bottom: 0.75em;
  padding: 16px;
}

.tiptap > * + * {
  margin-top: 0.75em;
}

.tiptap ul,
.tiptap ol {
  padding: 0 1rem;
}

.tiptap h1,
.tiptap h2,
.tiptap h3,
.tiptap h4,
.tiptap h5,
.tiptap h6 {
  line-height: 1.1;
}
</style>
