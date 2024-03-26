<template>
  <div id="app">
    <h1>{{message}}</h1>
    <todo-list></todo-list>
    <todo-list></todo-list>
    <todo-list></todo-list>
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TodoList from "./components/TodoList.vue";

export default {
  name: "App",
  components: {
    // HelloWorld
    TodoList
  },
  data: function() {
    return {
      message: "Hello Vue!"
    };
  }
};
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
