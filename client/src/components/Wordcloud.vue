<template>
  <div>
    <wordcloud
      :data="wordData"
      :rotate="rotateSettings"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true">
    </wordcloud>
  </div>
</template>

<script>
// import 'zingchart/es6';
// import zingchartVue from 'zingchart-vue';
import wordcloud from 'vue-wordcloud';

export default {
  name: 'WordCloud',
  data() {
    return {
      myColors: ['#ffffff', '#FF4151'],
      rotateSettings: {
        from: -45,
        to: 45,
        numOfOrientation: 3,
      },
    };
  },
  components: {
    // zingchart: zingchartVue,
    wordcloud,
  },
  props: {
    wordData: { type: Array, required: true },
  },
};
</script>

<style scoped>
div {
  width: 92%;
  margin: auto;
  margin-top: 15px;
  padding: 0;
}
</style>
