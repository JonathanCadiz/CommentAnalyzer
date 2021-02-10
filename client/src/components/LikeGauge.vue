<template>
  <div class="container">
    <VueSvgGauge
      class="gauge"
      :start-angle="-120"
      :end-angle="120"
      :value="gaugeData"
      :separator-step="0"
      :min="0"
      :max="100"
      :gauge-color="[{ offset: 0, color: '#FF4151'}, { offset: 100, color: '#FFC371'}]"
      :base-color="'#FFFFFF'"
      :scale-interval="5"
      :inner-radius="75"
    >
      <div class="inner-text">
        <p class="num">{{ String(gaugeData / 100).substring(2,4) }}</p>
        <p>% Likes</p>
      </div>
    </VueSvgGauge>
  </div>
</template>

<script>
import { VueSvgGauge } from 'vue-svg-gauge';

export default {
  name: 'LikeGauge',
  data() {
    return {
      likes: this.data.videoInfo.likes,
      dislikes: this.data.videoInfo.dislikes,
    };
  },
  components: {
    VueSvgGauge,
  },
  props: {
    data: {
      type: Object,
    },
  },
  computed: {
    gaugeData() {
      const likes = Number(this.data.videoInfo.likes);
      const dislikes = Number(this.data.videoInfo.dislikes);
      const totalCount = likes + dislikes;
      return (likes / totalCount) * 100;
    },
  },
};
</script>

<style scoped>
.container {
  width: 90%;
  height: 90%;
  margin-top: 4%;
  margin-bottom: 5%;
}

.inner-text {
  width: 50%;
  margin: auto;
  margin-top: 28%;
  text-align: center;
}

.inner-text p {
  max-width: 100px;
  color: white;
  margin: 0;
  font-weight: 700;
}

.num {
  font-size: 3.25em;
  line-height: 1em;
}
</style>
