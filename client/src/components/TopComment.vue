<template>
  <div class="trans-container">
    <h1>Top Comment</h1>
    <p>{{ '"' + getText + '"'}}</p>
    <p id="likes">{{ '-' + getLikes.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
      + ' likes'}}</p>
  </div>
</template>

<script>
export default {
  name: 'TopMenu',
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
  computed: {
    getText() {
      return this.data.data.topComment.text;
    },
    getLikes() {
      return this.data.data.topComment.likes;
    },
  },
};
</script>

<style scoped>
.trans-container {
  background-color: #ffd7cd49;
  width: 50%;
  min-height: 150px;
  margin: 50px auto 0 auto;
  padding: 2%;
}

h1 {
  color: white;
  font-size: 1.5em;
  font-weight: 700;
}

p {
  color: white;
  font-size: 2em;
  line-height: 1.4em;
  width: 100%;
  margin-top: auto;
  margin-bottom: auto;
  font-style: italic;
}

#likes {
  font-size: 1.3em;
  font-style: normal;
  margin-left: 5%;
}
</style>
