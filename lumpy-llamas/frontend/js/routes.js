import Home from './home-page.vue';
import Login from './login.vue';
import TicTacToe from './tic-tac-toe.vue';
import Forum from './thread-list.vue';
import Thread from './thread-view.vue';
import PostThread from './new-thread.vue';
import Newsfeed from './news-feed.vue';

const routes = [
  {
    path: '/home',
    alias: '/',
    name: 'home_page',
    component: Home,
  },
  {
    path: '/login',
    name: 'login_page',
    component: Login,
  },
  {
    path: '/games/tictactoe',
    name: 'tictactoe_page',
    component: TicTacToe,
  },
  {
    path: '/forum',
    name: 'forum',
    component: Forum,
  },
  {
    path: '/forum/new',
    name: 'new-thread',
    component: PostThread,
  },
  {
    path: '/forum/:id',
    name: 'thread-view',
    component: Thread,
  },
  {
    path: '/newsfeed',
    name: 'newsfeed',
    component: Newsfeed,
  },

];

export default routes;
