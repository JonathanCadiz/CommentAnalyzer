<template>
  <div class="trans-container row">
    <img :src="data['thumbnail']" />
    <div class="text">
      <h2>{{ data['title'] }}</h2>
      <div class="row">
        <p>{{ data['channel'] }}</p>
        <p>{{ '&#8226; ' + data['views'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
            + ' Views' }}</p>
        <p>{{ '&#8226; ' + data['commentCount'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
            + ' Comments' }}</p>
      </div>
      <br/>
      <p>Tags:</p>
      <ul class="row">
        <li v-for="tag in data['tags']" :key="tag">{{ tag }}</li>
      </ul>
    </div>
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
  padding: 60px 0px 60px 0px;
  margin: 0;
}

h2 {
  font-weight: 700;
}

img {
  height: 100%;
  margin-top: auto;
  margin-bottom: auto;
}

.row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  padding-left: 20px;
  justify-content: center;
}

.text {
  padding-left: 5%;
  width: 45%;
  margin-top: auto;
  margin-bottom: auto;
  color: white;
}

.row p {
  padding: 0px 15px 0px 0px;
  font-size: 1.1em;
}

.row li {
  margin: 0px 12px 0px 12px;
}

.text .row {
  justify-content:flex-start;
}
</style>
