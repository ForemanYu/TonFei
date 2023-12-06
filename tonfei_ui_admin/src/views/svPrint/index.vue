<template>
  <Designer :template="template" v-on="onDesigned" />
</template>

<script setup lang="ts">
import { ref } from "vue";
import "sv-p/style.css";
import { Designer } from "@sv-print/vue3";

let template = ref({});
const onDesigned = e => {
  console.log("onDesigned");
  console.log(e);
};
</script>
