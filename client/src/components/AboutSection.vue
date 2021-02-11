<template>
  <div class="trans-container">
    <h1>How Does it Work?</h1>
    <div class="about-text">
      <p>
        Commint extracts the YouTube video id from your url,
        and uses that id to request data from <a href="https://developers.google.com/youtube/v3">
        YouTube’s data API</a>.
        It’ll loop through all of your comments until every single comment,
        thread, and reply is saved, and then use Natural Language Processing
        (with <a href="https://spacy.io/">spaCy</a>) to remove irrelevant words and find keywords, nouns,
        adjectives, and verbs. Commint will also find what videos and websites
        your viewers link to, letting you gain insight to what timestamps of your
        video are most commonly referenced or what sites your audience thinks is
        relevant. Commint will then analyze and display all of this data in a clear,
        intuitive way to make sure you understand your audience.
      </p>
      <p>
        This project is actually open source, as well! Check out the source code on
        <a href="https://github.com/JonathanCadiz/CommentAnalyzer">GitHub</a>!
      </p>
    </div>
    <h1>And Who Made This?</h1>
    <div class="about-text">
      <p>
        I did! I’ll take this as an opportunity to shill myself a bit,
        if you’re not a developer, looking for a developer, or if you
        don’t particularly care and just want to see your comments, feel
        free to ignore this. I’m Jonathan, a Full Stack developer focusing
        in back-end development and automation. I love building end to end
        products, if you’d like to see more or get in contact with me, check
        out the links below to see my website, LinkedIn, and GitHub.
      </p>
    </div>
    <social-buttons></social-buttons>
  </div>
</template>

<script>
import SocialButtons from './SocialButtons.vue';

export default {
  name: 'About',
  components: {
    SocialButtons,
  },
};
</script>

<style scoped>
  .trans-container {
    background-color: #ffd7cd49
  }

  .about-text {
    width: 90%;
    margin-left: auto;
    margin-right: auto;
  }

  p, h1 {
    color: white;
  }

  h1 {
    text-align: center;
    font-size: 1.75em;
    font-weight: 700;
    padding-top: 35px;
    padding-bottom: 20px;
  }

  a {
    color: #9A0000;
  }
</style>
