<template>
  <div>
    <logo-button></logo-button>
    <request-section
    @passingData="saveData($event)"
    @passingLoading="startLoading()"></request-section>
    <div v-if="loading" id="loader">
      <loading-icon></loading-icon>
    </div>
    <analysis-section v-if="'data' in commentData" :data="commentData"></analysis-section>
    <about-section></about-section>
  </div>
</template>

<script>
import AboutSection from './AboutSection.vue';
import AnalysisSection from './AnalysisSection.vue';
import LoadingIcon from './LoadingIcon.vue';
import LogoButton from './Logo.vue';
import RequestSection from './RequestSection.vue';

export default {
  data() {
    return {
      commentData: {},
      loading: false,
    };
  },
  components: {
    RequestSection,
    AboutSection,
    LogoButton,
    AnalysisSection,
    LoadingIcon,
  },
  name: 'LandingPage',
  methods: {
    saveData(data) {
      this.commentData = data;
      this.loading = false;
    },
    startLoading() {
      this.loading = true;
    },
  },
};
</script>

<style scoped>
#loader {
  text-align: center;
  padding: 0px 0 100px 0;
}
</style>
