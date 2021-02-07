<template>
  <div>
    <logo-button></logo-button>
    <request-section></request-section>
    <about-section></about-section>
  </div>
</template>

<script>
import AboutSection from './AboutSection.vue';
import LogoButton from './Logo.vue';
import RequestSection from './RequestSection.vue';

export default {
  components: { RequestSection, AboutSection, LogoButton },
  name: 'LandingPage',
};
</script>

<style scoped>

</style>
