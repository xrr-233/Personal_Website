import { createRouter, createWebHashHistory } from 'vue-router'
import Index from "@/pages/Index.vue";

const routes = [
  { path: "/", name: "Index", component: Index },
  {
    path: '/gallery',
    name: 'Gallery',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('@/pages/Gallery.vue'),
    meta: {
      title: "xrr的作品集",
    }
  },
  { path: '/log', name: 'Log', component: () => import(/* webpackChunkName: "log" */ '@/pages/Log.vue') },
  { path: '/personal', name: 'Personal', component: () => import(/* webpackChunkName: "personal" */ '@/pages/Personal.vue') },
  { path: '/space', name: 'Space', component: () => import(/* webpackChunkName: "space" */ '@/pages/Space.vue'), meta: { title: "xrr的空间" } },
  { path: '/under_construction', name: 'UnderConstruction', component: () => import(/* webpackChunkName: "under_construction" */ '@/pages/UnderConstruction.vue') },
  { path: '/refresh_media', name: 'RefreshMedia', component: () => import(/* webpackChunkName: "refresh_media" */ '@/pages/RefreshMedia.vue') },
  {
    path: "/announcement/:id",
    component: () => import(/* webpackChunkName: "independent_page" */ '@/pages/IndependentPage.vue'),
    props: route => ({
      articleType: 'announcement',
      articleId: parseInt(route.params.id)
    })
  },
  {
    path: "/blog/:id",
    component: () => import(/* webpackChunkName: "independent_page" */ '@/pages/IndependentPage.vue'),
    props: route => ({
      articleType: 'blog',
      articleId: parseInt(route.params.id)
    })
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  linkActiveClass: 'router-link-activated'
})

// 全局路由守卫
router.afterEach((to) => {
  if(to.meta.title !== undefined)
    document.title = to.meta.title
  else
    document.title = "xrr的个人网站"
})

export default router
