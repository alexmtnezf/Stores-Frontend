from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

posts = []


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/blog')
def blog_page():
    return render_template('blog.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        global posts

        posts.append({
            'title': title,
            'content': content
        })

        return redirect(url_for('blog_page'))
    return render_template('new_post.html')


@app.route('/post/<string:title>')
def see_post(title):
    global posts

    for post in posts:
        if post['title'] == title:
            return render_template('post.html', post=post)

    return render_template('post.html', post=None)


@app.route('/restaurants/')
def restaurants():
    # rests = read_data.read_all(Restaurant)

    return render_template("restaurants.html")


@app.route("/restaurant/<int:restaurant_id>")
@app.route("/restaurant/<int:restaurant_id>/menu")
def restaurant_menu(restaurant_id):
    '''
    Function that returns the menu items for a restaurant
    :param int restaurant_id: Identifier for restaurant
    :return: string the web server response
    '''

    return render_template("menu.html")
    # try:
    #     restaurant, items = get_restaurant_menu(restaurant_id)
    # except NoResultFound:
    #     raise Exception("Not found")
    # else:
    #     return render_template("menu.html", restaurant=restaurant, items=items)


# Task 1: Create route for newMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    return render_template('newmenuitem.html', restaurant_id=restaurant_id)
    # if request.method == 'POST':
    #     mi = MenuItem(name=request.form.get('name'), price=request.form.get('price'),
    #                   description=request.form.get('description'), course=request.form.get('course'),
    #                   restaurant_id=restaurant_id)
    #     import create_data
    #     create_data.create(mi)
    #     flash("Menu Item Created!")
    #     return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    # else:
    #     return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    return render_template('editmenuitem.html')
    # import update_data
    # try:
    #     mi_item = read_data.read_by_id(MenuItem, {'id': menu_id})
    #
    # except NoResultFound:
    #     raise Exception('Not found')
    #
    # if request.method == 'POST':
    #
    #     update_data.update_data(mi_item, name=request.form.get('name'), price=request.form.get('price'),
    #                             description=request.form.get('description'), course=request.form.get('course'))
    #     flash("Menu Item Successfully Edited!")
    #     return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    # else:
    #
    #     return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu=mi_item)


# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    flash("Menu Item Successfully Deleted!")
    return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    # try:
    #     item_delete = read_data.read_by_id(MenuItem, {'id': menu_id})
    # except NoResultFound:
    #     raise Exception('Not found')
    # else:
    #     if request.method != 'POST':
    #         return render_template('deletemenuitem.html', item=item_delete)
    #     else:
    #         import delete_data
    #         delete_data.delete_data(item_delete)
    #         flash("Menu Item Successfully Deleted!")
    #         return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))


# Task 4: Create rout for new_restaurant function
@app.route('/restaurant/new', methods=['GET', 'POST'])
def new_restaurant():
    return render_template('newrestaurant.html')

    # if request.method == 'POST':
    #     import create_data
    #     newrest = Restaurant(name=request.form.get('name'))
    #     create_data.create(newrest)
    #     flash('New Restaurant Created')
    #     return redirect(url_for('restaurants'))
    # else:
    #     return render_template('newrestaurant.html')


# Task 5: Create route for edit_restaurant function
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    return render_template('editrestaurant.html')
    # try:
    #     restaurant = read_data.read_by_id(Restaurant, {'id': restaurant_id})
    #
    # except NoResultFound:
    #     raise Exception('Not found')
    #
    # if request.method == 'POST':
    #     import update_data
    #     update_data.update_data(restaurant, name=request.form.get('name'))
    #     flash("Restaurant Successfully Edited!")
    #     return redirect(url_for('restaurants'))
    # else:
    #     return render_template('editrestaurant.html', restaurant=restaurant)


# Task 6: Create route for delete_restaurant function
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    return render_template('deleterestaurant.html')
    # try:
    #     restaurant = read_data.read_by_id(Restaurant, {'id': restaurant_id})
    # except NoResultFound:
    #     raise Exception('Not found')
    # else:
    #     if request.method != 'POST':
    #         return render_template('deleterestaurant.html', restaurant=restaurant)
    #     else:
    #         import delete_data
    #         flash("Restaurant Successfully Deleted!".format(name=restaurant.name))
    #         delete_data.delete_data(restaurant)
    #         return redirect(url_for('restaurants'))


#
# def get_restaurant_menu(restaurant_id):
#     restaurant = read_data.read_by_id(Restaurant, {'id': restaurant_id})
#     kwargs = {'restaurant_id': restaurant.id}
#     items = read_data.find_by(MenuItem, kwargs)
#     return restaurant, items


if __name__ == '__main__':
    app.debug = True
    app.run()
