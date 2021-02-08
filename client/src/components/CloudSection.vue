<template>
  <div class="trans-container">
    <div class="row">
      <h1>What're People Saying?</h1>
      <filter-buttons></filter-buttons>
    </div>
    <word-cloud id="cloud" :word-data="data['data']['words']"></word-cloud>
    <top-word-list :word-data="data['data']['words']"></top-word-list>
  </div>
</template>

<script>
import FilterButtons from './CloudFilterButtons.vue';
import TopWordList from './TopWordList.vue';
import WordCloud from './Wordcloud.vue';

export default {
  name: 'CloudSection',
  data() {
    return {
    };
  },
  components: {
    WordCloud,
    TopWordList,
    FilterButtons,
  },
  props: {
    data: {
      type: Object,
    },
  },
};
</script>

<style scoped>
.trans-container {
  background-color: #ffd7cd49;
  padding-left: 20px;
  padding-top: 20px;
}

h1 {
  font-size: 1.75em;
  font-weight: 700;
  color: white;
}

.row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  padding-left: 20px;
  justify-content: space-between;
}
</style>
