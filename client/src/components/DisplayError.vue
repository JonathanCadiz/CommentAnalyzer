<template>
  <div class="trans-container">
    <p>{{ data.error }}</p>
  </div>
</template>

<script>
export default {
  name: 'DisplayError',
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
  },
};
</script>

<style scoped>
.trans-container {
  background-color: #ffd7cd49;
  width: 50%;
  min-height: 150px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
}

p {
  color: white;
  font-size: 2em;
  width: 100%;
  font-style: italic;
}
</style>
