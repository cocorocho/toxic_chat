import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Register from "@/components/Register.vue"
import Login from "@/components/Login.vue"


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: "/register",
    name: "Register",
    component: Register
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
