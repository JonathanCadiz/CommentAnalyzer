<template>
  <div>
    <h1>REVOLUTIONIZE YOUR FEEDBACK</h1>
    <p>
      <strong>Commint</strong> reads through <strong>all</strong>
      the comments on your video to help you <strong>see</strong>
      what your audience is trying to tell you.
    </p>
    <p id="bottom-text">
      Whether you’re looking for <strong>video ideas</strong>,
      trying to gauge the <strong>response to a new video</strong>
      , or just want to see what your audience is up to, Commint
      helps you to <strong>understand</strong> your users!
    </p>
  </div>
</template>

<script>
export default {
  name: 'Title',
};
</script>

<style scoped>
  h1, p {
    color: white;
    text-align: center;
  }

  strong, h1 {
    font-weight:700;
  }

  h1 {
    margin-top: 50px;
    margin-bottom: 50px;
  }

  #bottom-text {
    width: 65%;
    margin-left: auto;
    margin-right: auto;
  }
</style>
