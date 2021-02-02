<template>
  <div class="container">
    <form>
      <label>url</label>
      <input v-model="req.url" id="url"/>
      <label>key</label>
      <input v-model="req.key" id="key"/>
    </form>
    <button class="btn btn-primary" @click.prevent="submitted">Submit!</button>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
      req: {
        url: '',
        key: '',
      },
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch(() => {
        });
    },
    submitted() {
      axios.post('http://localhost:5000/ping', {
        url: this.req.url,
        key: this.req.key,
      })
        .then((response) => {
          console.log(response.data);
          this.msg = response.data;
        })
        .catch();
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
