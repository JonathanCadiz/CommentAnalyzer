import Vue from 'vue';
import Router from 'vue-router';
import VueMeta from 'vue-meta';
import LandingPage from '../components/LandingPage.vue';

Vue.use(Router);
Vue.use(VueMeta);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '',
      name: 'CommentAnalyzer',
      component: LandingPage,
      metaInfo: {
        title: 'Commint | Get Your Feedback',
      },
    },
  ],
});
