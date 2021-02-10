<template>
  <div class="container">
    <title-text id="title"></title-text>
    <video-input id="videoInput"
    @gotResponse="passResponse($event)"
    @startLoading="passLoading()"></video-input>
  </div>
</template>

<script>
import TitleText from './Title.vue';
import VideoInput from './VideoInput.vue';

export default {
  components: { VideoInput, TitleText },
  name: 'RequestSection',
  methods: {
    passResponse(data) {
      this.$emit('passingData', data);
    },
    passLoading() {
      this.$emit('passingLoading');
    },
  },
};
</script>

<style scoped>
  #videoInput {
    width: 65%;
    margin-top: 80px;
    margin-bottom: 80px;
  }

  .container {
    padding: 15px;
  }
</style>
