<template>
  <div>
    <a href="https://www.google.com"><img :src="image1"/></a>
  </div>
</template>

<script>
import logo from '@/assets/commint.png';

export default {
  name: 'LogoButton',
  data() {
    return {
      image1: logo,
    };
  },
  methods: {

  },
};
</script>

<style scoped>
  div {
    text-align: center;
    padding-bottom: 60px;
  }

  a {
    float: left;
    margin: 20px;
  }

  a, img {
    width: 10%;
    min-width: 125px;
  }
</style>
