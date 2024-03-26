<template>
  <span>
    <input type="text" placeholder="请输入待办事项" v-model="todo_input" v-on:keyup.enter="submit" />
    <button type="button" v-on:click="submit">保存</button>
    <ul>
      <li v-for="item in todoItems">
        <input type="checkbox" v-model="item.done" />
        <span v-if="!item.done">{{ item.title }}</span>
        <span v-else style="text-decoration: line-through;">{{item.title}}</span>
      </li>
    </ul>
  </span>
</template>

<script>
export default {
  name:"TodoList",
  data: function() {
    return {
      todo_input: "",
      todoItems: [
        {
          title: "学习 vue",
          done: true //是否已经完成
        },
        {
          title: "学习 webpack",
          done: false //是否已经完成
        },
        {
          title: "做个小项目",
          done: false //是否已经完成
        }
      ]
    };
  },
  methods: {
    submit(event) {
      this.todoItems.push({ title: this.todo_input, done: false });
    }
  }
};
</script>

<style>
</style>