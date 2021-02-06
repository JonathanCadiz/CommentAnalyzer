import Vue from 'vue';
import Router from 'vue-router';
import VideoInput from '../components/VideoInput.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '',
      name: 'CommentAnalyzer',
      component: VideoInput,
    },
  ],
});
