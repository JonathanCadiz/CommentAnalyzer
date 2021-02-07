<template>
  <div>
    <request-section></request-section>
    <about-section></about-section>
  </div>
</template>

<script>
import AboutSection from './AboutSection.vue';
import RequestSection from './RequestSection.vue';

export default {
  components: { RequestSection, AboutSection },
  name: 'LandingPage',
};
</script>

<style scoped>

</style>
