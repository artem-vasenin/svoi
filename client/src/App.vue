<template>
  <v-app>
    <Header />
    <v-main class="main">
      <v-container class="main-container">
        <router-view/>
      </v-container>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Header from '@/components/app/Header';
import Footer from '@/components/app/Footer';

export default {
  name: 'App',
  components: { Footer, Header },
  data: () => ({}),
}
</script>

<style lang="scss">
.main {
  flex: 1;
  background: #C9E7DDFF;
}
.main-container {
  display: flex;
  flex-direction: column;
  background: #C9E7DDFF url("./assets/reg-bg.jpg") no-repeat bottom right;
  background-size: contain;
  height: 100%;
}
</style>
