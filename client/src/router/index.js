import Vue from 'vue';
import Router from 'vue-router';
import LandingPage from '../components/LandingPage.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '',
      name: 'CommentAnalyzer',
      component: LandingPage,
    },
  ],
});
