import { createRouter, createWebHistory } from 'vue-router'
import Tracker from "../views/Tracker.vue"

const routes = [
  {
    path: '/',
    name: 'Tracker',
    component: Tracker
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
