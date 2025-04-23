<template>
  <nav class="nav">
    <ul class="nav__list">
      <li class="nav__list-item" v-for="(i, idx) in list" :key="idx">
        <router-link class="nav__list-link" :to="i.url">{{i.title}}</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'TopMenu',
  data() {
    return {
      list: [
        { url: '/', title: 'Знакомства' },
        { url: '/', title: 'Форум' },
        { url: '/', title: 'Информация' },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.nav {
  &__list {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 60px;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  &__list-link {
    font-size: 18px;
    color: white;
    text-decoration: none;
    font-weight: bold;
  }
}
</style>
