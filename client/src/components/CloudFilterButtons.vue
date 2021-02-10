<template>
  <div>
    <button type="button" class="filter-button selected"
    @click="selectButton(1)">Words</button>
    <button type="button" class="filter-button"
    @click="selectButton(2)">Entities</button>
    <button type="button" class="filter-button"
    @click="selectButton(3)">Nouns</button>
    <button type="button" class="filter-button"
    @click="selectButton(4)">Adj.</button>
    <button type="button" class="filter-button"
    @click="selectButton(5)">Verbs</button>
  </div>
</template>

<script>
export default {
  name: 'FilterButtons',
  data() {
    return {
    };
  },
  components: {
  },
  props: {
  },
  methods: {
    selectButton(index) {
      const buttonList = document.getElementsByTagName('button');
      const buttons = [0, 'words', 'entities', 'nouns', 'adjectives', 'verbs'];
      buttonList.forEach((button) => { button.classList.remove('selected'); });
      buttonList[index].classList.add('selected');
      this.$emit('filtered', buttons[index]);
    },
  },
};
</script>

<style scoped>
.filter-button {
  margin: 5px;
  min-height: 35px;
  min-width: 75px;
  border: none;
  background-color: white;
  color: #FF4152;
  font-size: 1.1em;
}

.selected {
  background-color: #FF4152;
  color: white;
}

button:hover {
  background-color:rgb(238, 238, 238);
}

.selected:hover {
  background-color: #FF4152;
}
</style>
