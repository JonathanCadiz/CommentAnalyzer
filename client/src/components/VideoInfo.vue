<template>
  <div class="trans-container">
    <h1>What're People Saying?</h1>
  </div>
</template>

<script>
export default {
  name: 'VideoInfo',
  data() {
    return {
    };
  },
  components: {
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
