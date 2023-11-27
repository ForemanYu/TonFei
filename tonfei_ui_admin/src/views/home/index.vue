<template>
  <!--  <div class="home card">-->
  <!--    <img class="home-bg" src="@/assets/images/welcome.png" alt="welcome" />-->
  <!--  </div>-->
  <div class="home">
    <el-card class="box-card">
      <div v-for="(o, index) in data.objs" :key="index" class="text item">
        <div style="width: 800px">{{ o.key + "-" + o.content }}</div>
      </div>
    </el-card>
  </div>
  <div class="home-bottom">
    <el-affix position="bottom" :offset="50">
      <el-input v-model="data1" placeholder="与文心一言交谈" style="width: 500px">
        <template #append>
          <el-button @click="sendPost"> 发送</el-button>
        </template>
      </el-input>
    </el-affix>
  </div>
</template>

<script setup lang="ts" name="home">
import { reactive, ref } from "vue";

const data = reactive<{
  objs: myObj[];
}>({
  objs: []
});

interface myObj {
  key: number;
  content: string;
}

const data1 = ref<string>("");
const response = ref("");
const controller = ref(new AbortController());
const isStopped = ref(false);

async function sendPost() {
  controller.value = new AbortController();
  response.value = "";
  isStopped.value = false;
  const res = await fetch("http://127.0.0.1:8008/dialogue/questions?content=" + data1.value, {
    method: "POST"
  });
  const reader = res.body.getReader();
  data.objs.push({ key: 1, content: "" });
  while (true) {
    if (isStopped.value) break;
    const { done, value } = await reader.read();
    if (done) break;

    const objToUpdate = data.objs.find(obj => obj.key === 1);
    if (objToUpdate) {
      objToUpdate.content += new TextDecoder().decode(value);
    }
  }
}
</script>

<style scoped lang="scss">
@import "./index.scss";
</style>
