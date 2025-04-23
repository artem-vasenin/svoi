<template>
<footer class="footer">
  <v-container>
    <v-row>
      <v-col cols="2">
        <v-img
          :src="require('../../assets/logo.png')"
          class="logo"
          contain
          height="50"
          width="50"
        />
      </v-col>
      <v-col cols="8" class="text-center d-flex align-center text-white justify-center">Политика конфиденциальности</v-col>
      <v-col cols="2" class="d-flex align-center">
        <v-btn density="default" variant="text" icon="md:phone" size="x-small" color="white" class="icon"/>
        <v-btn density="default" variant="text" icon="md:facebook" size="x-small" color="white" class="icon"/>
        <v-btn density="default" variant="text" icon="md:facebook" size="x-small" color="white" class="icon"/>
      </v-col>
    </v-row>
  </v-container>
</footer>
</template>

<script>
export default {
  name: 'Footer'
};
</script>

<style scoped lang="scss">
.footer {
  background-color: #002513;
  min-height: 56px;
}
.logo {
  border-radius: 50%;
}
.icon {
  margin: 0 6px;

  &:first-child {
    margin-left: 0;
  }

  &:last-child {
    margin-right: 0;
  }
}
</style>
