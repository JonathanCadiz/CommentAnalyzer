<template>
  <div class="container">
    <video-input id="videoInput"></video-input>
  </div>
</template>

<script>
import VideoInput from './VideoInput.vue';

export default {
  components: { VideoInput },
  name: 'RequestSection',
};
</script>

<style scoped>
  #videoInput {
    width: 65%;
  }

  .container {
    padding: 15px;
  }
</style>
