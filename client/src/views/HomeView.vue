<template>
  <HelloWorld :text="text" />
</template>

<script>
import { defineComponent } from 'vue';

// Components
import HelloWorld from '../components/HelloWorld.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    HelloWorld,
  },
  data() {
    return ({
      text: '',
    });
  },
  methods: {
    async getHomePage() {
      await fetch('http://localhost:8000')
          .then(res => {
            if (!res.ok) throw new Error('Что-то пошло не так');
            return res.json();
          })
          .then(data => {
            this.text = data;
          })
          .catch(err => {
            console.error('Ошибка запроса:', err);
          });
    },
  },
  async mounted() {
    await this.getHomePage();
  }
});
</script>
