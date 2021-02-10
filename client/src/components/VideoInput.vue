<template>
  <div class="container">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div>
      <form>
        <input v-model="req.url" id="url"
        placeholder="Enter the link to a YouTube video to get started!"/>
      </form>
    <button class="btn btn-primary" @click.prevent="submitted">
      <i class="fa fa-play"></i>
    </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VideoInput',
  data() {
    return {
      msg: '',
      req: {
        url: '',
      },
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/videorequest';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch(() => {
        });
    },
    submitted() {
      this.$emit('startLoading');
      axios.post('http://localhost:5000/videorequest', {
        url: this.req.url,
      })
        .then((response) => {
          this.msg = response.data;
          this.$emit('gotResponse', this.msg);
        })
        .catch();
    },
  },
  created() {
  },
};
</script>

<style scoped>
  input {
    float: left;
    width: 79%;
    min-height: 50px;
    border: none;
    padding: 10px;
    -webkit-box-shadow:inset 0 0 10px rgba(0, 0, 0, 0.52);
       -moz-box-shadow:inset 0 0 10px rgba(0, 0, 0, 0.52);
            box-shadow:inset 0 0 10px rgba(0, 0, 0, 0.52);
  }

  button {
    width: 16%;
    min-height: 50px;
    margin-left: 20px;
    background-color: #FF4152;
    border: none;
    border-radius: 0;
    font-size: 150%;
  }

  button:hover {
    background-color: #ca3441;
  }

  button:focus {
    background-color: #FF4152;
  }

  button:active {
    background-color: #FF4152;
  }
</style>
