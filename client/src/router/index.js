import { createRouter, createWebHashHistory } from 'vue-router'
import Index from "@/components/Index";
import ClockMaster from "@/components/ClockMaster";
import Announcement from "@/components/Announcement";
import Divination from "@/components/Divination";
import UnderConstruction from "@/components/UnderConstruction";

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
    component: () => import('../components/Space.vue'),
  },
  {
    path: '/clock_master',
    name: 'ClockMaster',
    component: ClockMaster,
  },
  {
    path: '/announcement',
    name: 'Announcement',
    component: Announcement,
  },
  {
    path: '/divination',
    name: 'Divination',
    component: Divination,
  },
  {
    path: '/under_construction',
    name: 'UnderConstruction',
    component: UnderConstruction,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
