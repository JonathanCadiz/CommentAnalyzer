<template>
  <div class="container">
    <form>
      <label>url</label>
      <input v-model="req.url" id="url"/>
    </form>
    <button class="btn btn-primary" @click.prevent="submitted">Submit!</button>
    <p>{{ msg }}</p>
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
      axios.post('http://localhost:5000/videorequest', {
        url: this.req.url,
      })
        .then((response) => {
          console.log(response.data);
          this.msg = response.data;
        })
        .catch();
    },
  },
  created() {
    this.getData();
  },
};
</script>
