from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/morephoto')
def morephoto():
    # List of images to display
    images = ['jacket.png', 'jacket2.png', 'jacket3.png']
    return render_template('morephoto.html', images=images)

images = ['jacket.png', 'jacket2.png', 'jacket3.png']

@app.route('/bigphoto')
def bigphoto():
    selected_img = request.args.get('img')
    if selected_img not in images:
        selected_img = images[0]  # default to first image if invalid or missing
    return render_template('bigphoto.html', images=images, selected_img=selected_img)

if __name__ == '__main__':
    app.run(debug=True)
