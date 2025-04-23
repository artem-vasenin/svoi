<template>
<header class="header">
  <v-container>
    <v-row>
      <v-col cols="1" class="pt-0 pb-0">
        <v-img
          :src="require('../../assets/logo.png')"
          class="logo"
          contain
          height="50"
          width="50"
        />
      </v-col>
      <v-col cols="10"><TopMenu/></v-col>
      <v-col cols="1" class="pt-0 pb-0 text-right">
        <v-btn density="default" variant="text" size="48">
          <v-icon icon="md:output" color="white" size="30"/>
        </v-btn>
      </v-col>
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
  background-color: #002513;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16);
}
.logo {
  border-radius: 50%;
}
</style>
