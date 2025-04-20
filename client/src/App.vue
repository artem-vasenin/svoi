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
.main-container {
  display: flex;
  flex-direction: column;
}
.main {
  flex: 1;
}
</style>
