<template>
<header class="header">
  <v-container>
    <v-row>
      <v-col cols="2">LOGO</v-col>
      <v-col cols="8"><TopMenu/></v-col>
      <v-col cols="2">LOGIN</v-col>
    </v-row>
  </v-container>
</header>
</template>

<script>
import TopMenu from '@/components/app/TopMenu.vue';

export default {
  name: 'Header',
  components: {TopMenu},
};
</script>

<style scoped lang="scss">
.header {
  background-color: #C4C4C4;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16);
}
</style>
