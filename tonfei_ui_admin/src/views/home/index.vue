<template>
  <!--  <div class="home card">-->
  <!--    <img class="home-bg" src="@/assets/images/welcome.png" alt="welcome" />-->
  <!--  </div>-->
  <div class="home">
    <el-card class="box-card">
      <div v-for="(o, index) in data.objs" :key="index" class="text item">
        <div style="width: 800px">{{ o.user + "-" + o.age }}</div>
      </div>
    </el-card>
  </div>
  <div class="home-bottom">
    <el-affix position="bottom" :offset="50">
      <el-input placeholder="与文心一言交谈" style="width: 500px">
        <template #append>
          <el-button @click="onSubmit"> 发送</el-button>
        </template>
      </el-input>
    </el-affix>
  </div>
</template>

<script setup lang="ts" name="home">
import { reactive } from "vue";

const data = reactive<{
  objs: myObj[];
}>({
  objs: []
});

interface myObj {
  user: string;
  age: number;
}

const onSubmit = () => {
  const eventSource = new EventSource(
    "http://127.0.0.1:8008/dialogue/questions?content=%E7%8E%B0%E5%9C%A8%E7%9A%84%E6%97%B6%E9%97%B4%E6%98%AF"
  );

  eventSource.addEventListener("message", event => {
    // 处理接收到的事件数据
    const eventData = JSON.parse(event.data);
    // 进行相应的操作
    console.log(eventData);
  });

  eventSource.addEventListener("error", error => {
    // 处理错误
    console.error("EventSource error:", error);
  });
  // data.objs.push({ user: "文心一言", age: 18 });
};
</script>

<style scoped lang="scss">
@import "./index.scss";
</style>
