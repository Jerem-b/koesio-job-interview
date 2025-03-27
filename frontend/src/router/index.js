import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Authors from '@/views/Authors.vue';
import EditAuthor from '@/views/EditAuthor.vue';
import Books from '@/views/Books.vue';
import EditBook from '@/views/EditBook.vue';
import Users from '@/views/Users.vue';
import Borrows from '@/views/Borrows.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/authors',
    name: 'Authors',
    component: Authors,
  },
  {
    path: '/authors/:id',
    name: 'edit-author',
    component: EditAuthor,
    props: true,
  },
  {
    path: '/books',
    name: 'Books',
    component: Books,
  },
  {
    path: '/books/:id',
    name: 'edit-book',
    component: EditBook,
    props: true,
  },
  {
    path: '/users',
    name: 'Users',
    component: Users,
  },
  {
    path: '/borrows',
    name: 'Borrows',
    component: Borrows,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
