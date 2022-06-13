import { createRouter, createWebHashHistory } from 'vue-router'
import Index from "@/pages/Index";

const routes = [
  {
    path: "/",
    name: "Index",
    component: Index,
  },
  {
    path: '/space',
    name: 'Space',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('@/pages/Space.vue'),
    meta: {
      title: "xrr的空间"
    }
  },
  {
    path: '/under_construction',
    name: 'UnderConstruction',
    component: () => import('@/pages/UnderConstruction.vue'),
  },
  {
    path: '/personal',
    name: 'Personal',
    component: () => import('@/pages/Personal.vue'),
  },
  {
    path: '/refresh_media',
    name: 'RefreshMedia',
    component: () => import('@/pages/RefreshMedia.vue'),
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// 全局路由守卫
router.afterEach((to) => {
  if(to.meta.title !== undefined)
    document.title = to.meta.title
  else
    document.title = "xrr的个人网站"
})

export default router
