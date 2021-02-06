import Vue from 'vue';
import Router from 'vue-router';
import RequestSection from '../components/RequestSection.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '',
      name: 'CommentAnalyzer',
      component: RequestSection,
    },
  ],
});
