<template>
  <div class="row">
    <div class="trans-container">
      <like-gauge :data="data"></like-gauge>
    </div>
    <div class="trans-container column">
      <p>{{ percentLiked + '%' }}</p>
      <p class="small-text">of your viewers liked vs</p>
      <p>{{ percentDisliked + '%' }}</p>
      <p class="small-text">of your viewers disliked</p>
    </div>
    <div class="trans-container column">
      <p>{{ percentCommented + '%' }}</p>
      <p class="small-text">of your viewers commented</p>
    </div>
    <div class="trans-container column">
      <p>{{ topAdjective.charAt(0).toUpperCase() + topAdjective.slice(1) }}</p>
      <p class="small-text">Top Adjective</p>
    </div>
  </div>
</template>

<script>
import LikeGauge from './LikeGauge.vue';

export default {
  name: 'KeyMetrics',
  data() {
    return {
    };
  },
  components: {
    LikeGauge,
  },
  props: {
    data: {
      type: Object,
    },
  },
  computed: {
    percentLiked() {
      const likes = Number(this.data.videoInfo.likes);
      const views = Number(this.data.videoInfo.views);
      return Math.round((likes / views) * 10000) / 100;
    },
    percentDisliked() {
      const dislikes = Number(this.data.videoInfo.dislikes);
      const views = Number(this.data.videoInfo.views);
      return Math.round((dislikes / views) * 10000) / 100;
    },
    percentCommented() {
      const comments = Number(this.data.videoInfo.commentCount);
      const views = Number(this.data.videoInfo.views);
      return Math.round((comments / views) * 10000) / 100;
    },
    topAdjective() {
      return this.data.data.adjectives[0].name;
    },
  },
};
</script>

<style scoped>
.trans-container {
  background-color: #ffd7cd49;
  width: 20%;
  min-height: 100px;
  margin-left: 1.75%;
  margin-right: 1.75%;
  text-align: center;
}

.column {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  flex-direction: column;
}

.row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  margin-top: 50px;
  padding-left: 20px;
  justify-content: center;
}

p {
  color: white;
  font-size: 3em;
  font-weight: 700;
  line-height: 1.1em;
  margin: 4px;
  width: 100%;
}

.small-text {
  font-size: 1em;
}
</style>
