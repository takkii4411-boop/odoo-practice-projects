

from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class ToDo(CustomerPortal):
    @http.route(['/my/tasks', '/my/tasks/page/<int:page>'], type='http', auth='user', website=True)
    def portal_my_tasks(self, page=1, search=None, sortby=None, **kw):
        TaskModel = request.env['todo.pro']
        domain = []

        searchbar_sortings = {
            'date': {'label': 'Date', 'order': 'date desc'},
            'name': {'label': 'Name (A-Z)', 'order': 'name asc'},
            'new': {'label': 'Newest', 'order': 'create_date desc'},
            'older': {'label': 'Oldest', 'order': 'create_date asc'},
        }

        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        if search:
            domain += ['|','|', ('name', 'ilike', search), ('description', 'ilike', search), ('task_order', 'ilike',search )]

        task_count = TaskModel.sudo().search_count(domain)
        rpg = 5
        pager = portal_pager(
            url="/my/tasks",
            total=task_count,
            page=page,
            step=rpg,
            url_args={'search': search, 'sortby': sortby}
        )

        tasks = TaskModel.sudo().search(domain, limit=rpg, offset=pager['offset'], order=order)

        vals = {
            'tasks': tasks,
            'page_name': 'todo_task_portal',
            'pager': pager,
            'default_url': '/my/tasks',
            'search': search,
            'sortby': sortby,
            'searchbar_sortings': searchbar_sortings,
        }

        return request.render('task_manegment.portal_my_tasks', vals)

    @http.route(['/my/tasks/new'], type='http', auth='user', website=True)
    def portal_task_create(self):
        return request.render('task_manegment.portal_todo_form', {
            'page_name': 'todo_form',
        })

    @http.route(['/my/tasks/save'], type='http', auth='user', methods=['POST'], website=True)
    def portal_task_save(self, **post):
        vals = {
            'name': post.get('name'),
            'date': post.get('date'),
            'description': post.get('description'),
        }

        task_id = post.get('task_id')
        print(task_id)

        if task_id:
            task = request.env['todo.pro'].sudo().browse(int(task_id))
            if task.exists():
                task.write(vals)
        else:
            request.env['todo.pro'].sudo().create(vals)

        return request.redirect('/my/tasks')

    @http.route(['/my/tasks/<int:task_id>/edit'], type='http', auth='user', website=True)
    def portal_task_edit(self, task_id):
        task = request.env['todo.pro'].sudo().browse(task_id)
        if not task.exists():
            return request.render("website.404")

        return request.render('task_manegment.portal_todo_form', {
            'task': task,
            'page_name': 'todo_form',
        })

    @http.route(['/my/tasks/<int:task_id>/delete'], type='http', auth='user', website=True)
    def portal_task_delete(self, task_id):
        task = request.env['todo.pro'].sudo().browse(task_id)
        if task.exists():
            task.unlink()
        return request.redirect('/my/tasks')