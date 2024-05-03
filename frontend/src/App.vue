<template>
  <v-app>
    <v-app-bar height="130" app color="brown lighten-1" dark  hide-on-scroll>
      <v-toolbar-title class="mx-auto text-h4 title"> Bakery </v-toolbar-title>
      <v-btn text small class="ml-1" v-for="menu in menus" :key="menu.text" :to="menu.url">
        {{ menu.text }}
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    menus: [
      { text: 'Home', url: '/' },
      { text: 'Table', url: '/table' },
    ],
  }),
};
</script>

<style>
#app {
  font-family: Avenir, Comic, Helvetica, Arial, sans-serif;
}
</style>
