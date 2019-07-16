import Vue from 'vue'
import Router from 'vue-router'
import VueFormGenerator from 'vue-form-generator'

import ListNote from '@/components/Note/ListNote'
import EditNote from '@/components/Note/EditNote'
import DeleteNote from '@/components/Note/DeleteNote'
 
Vue.use(Router)
Vue.use(VueFormGenerator)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ListNote',
      component: ListNote
    },
    {
      path: '/:noteId/edit',
      name: 'EditNote',
      component: EditNote
    },
    {
      path: '/:noteId/delete',
      name: 'DeleteNote',
      component: DeleteNote
    }
  ],
  mode: 'history'
})
