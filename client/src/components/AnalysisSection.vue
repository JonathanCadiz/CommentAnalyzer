<template>
  <div>
    <video-info :data="data['videoInfo']"></video-info>
    <key-metrics :data="data"></key-metrics>
    <top-comment :data="data"></top-comment>
    <cloud-section id="cloud" :data="data"></cloud-section>
  </div>
</template>

<script>
import CloudSection from './CloudSection.vue';
import KeyMetrics from './KeyMetrics.vue';
import TopComment from './TopComment.vue';
import VideoInfo from './VideoInfo.vue';

export default {
  name: 'AnalysisSection',
  data() {
    return {
    };
  },
  components: {
    CloudSection,
    VideoInfo,
    KeyMetrics,
    TopComment,
  },
  props: {
    data: {
      type: Object,
    },
  },
};
</script>

<style scoped>
#cloud {
  width: 85%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
