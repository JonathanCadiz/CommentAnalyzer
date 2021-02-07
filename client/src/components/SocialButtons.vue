<template>
  <div>
    <a href="https://www.google.com"><img :src="image1"/></a>
    <a href="https://www.google.com"><img :src="image2"/></a>
    <a href="https://www.google.com"><img :src="image3"/></a>
  </div>
</template>

<script>
import site from '@/assets/site.png';
import git from '@/assets/github.png';
import linked from '@/assets/linkedin.png';

export default {
  name: 'SocialButtons',
  data() {
    return {
      image1: site,
      image2: git,
      image3: linked,
    };
  },
  methods: {

  },
};
</script>

<style scoped>
  div {
    text-align: center;
    padding-top: 30px;
    padding-bottom: 60px;
  }

  a {
    margin: 30px;
  }

  a, img {
    max-height: 40px;
    max-width: 40px;
  }
</style>
