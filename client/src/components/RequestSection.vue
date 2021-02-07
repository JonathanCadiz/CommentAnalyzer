<template>
  <div class="container">
    <title-text id="title"></title-text>
    <video-input id="videoInput"></video-input>
  </div>
</template>

<script>
import TitleText from './Title.vue';
import VideoInput from './VideoInput.vue';

export default {
  components: { VideoInput, TitleText },
  name: 'RequestSection',
};
</script>

<style scoped>
  #videoInput {
    width: 65%;
    margin-top: 60px;
    margin-bottom: 60px;
  }

  .container {
    padding: 15px;
  }
</style>
