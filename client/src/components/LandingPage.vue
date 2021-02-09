<template>
  <div>
    <logo-button></logo-button>
    <request-section @passingData="saveData($event)"></request-section>
    <analysis-section v-if="'data' in commentData" :data="commentData"></analysis-section>
    <about-section></about-section>
  </div>
</template>

<script>
import AboutSection from './AboutSection.vue';
import AnalysisSection from './AnalysisSection.vue';
import LogoButton from './Logo.vue';
import RequestSection from './RequestSection.vue';

export default {
  data() {
    return {
      commentData: {},
    };
  },
  components: {
    RequestSection,
    AboutSection,
    LogoButton,
    AnalysisSection,
  },
  name: 'LandingPage',
  methods: {
    saveData(data) {
      this.commentData = data;
    },
  },
};
</script>

<style scoped>

</style>
