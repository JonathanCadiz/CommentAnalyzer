<template>
  <div>
    <h2>Most Common Words</h2>
    <div class="row">
      <ol>
        <li v-for="word in wordData.slice(0,10)" :key="word.name">
          <span class="left">{{ word.name.charAt(0).toUpperCase() + word.name.slice(1) }}</span>
          <span class="right">{{ '- ' + word.value }}</span>
        </li>
      </ol>
      <ol start="11">
        <li v-for="word in wordData.slice(10,20)" :key="word.name">
          <span class="left">{{ word.name.charAt(0).toUpperCase() + word.name.slice(1) }}</span>
          <span class="right">{{ '- ' + word.value }}</span>
        </li>
      </ol>
      <ol start="21">
        <li v-for="word in wordData.slice(20,30)" :key="word.name">
          <span class="left">{{ word.name.charAt(0).toUpperCase() + word.name.slice(1) }}</span>
          <span class="right">{{ '- ' + word.value }}</span>
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopWordList',
  data() {
    return {
    };
  },
  components: {
  },
  props: {
    wordData: { type: Array, required: true },
  },
};
</script>

<style scoped>
div {
  color: white;
  margin-top: 0;
  width: 100%;
  padding-bottom: 15px;
}

.row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  padding-left: 20px;
  padding-right: 20px;
  justify-content: space-between;
}

ol {
  margin: 0;
  padding-left: 20px;
  width: 25%;
}

h2 {
  font-size: 1.25em;
  margin-bottom: 15px;
}

.left {
  float: left;
}

.right {
  float: right;
}
</style>
