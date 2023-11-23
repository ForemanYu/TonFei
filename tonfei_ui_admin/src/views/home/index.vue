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
  data.objs.push({ user: "文心一言", age: 18 });
};
</script>

<style scoped lang="scss">
@import "./index.scss";
</style>
